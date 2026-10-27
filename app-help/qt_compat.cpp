// Standalone consumer probe linked to the application's own Qt installation.
// Run against disposable copies: Qt may modify the collection/search index.
#include <QApplication>
#include <QHelpEngine>
#include <QHelpSearchEngine>
#include <QHelpContentModel>
#include <QNetworkAccessManager>
#include <QNetworkReply>
#include <QNetworkRequest>
#include <QBuffer>
#include <QTimer>
#include <QElapsedTimer>
#include <QThread>
#include <QWebView>
#include <QWebFrame>
#include <QPainter>
#include <QImage>
#include <QJsonDocument>
#include <QJsonObject>
#include <QJsonArray>
#include <QFile>
#include <QDir>
#include <QCryptographicHash>
#include <functional>
#include <stdexcept>

static void require(bool ok, const char *message) {
    if (!ok) throw std::runtime_error(message);
}
static void until(std::function<bool()> ready, int ms = 120000) {
    QElapsedTimer timer; timer.start();
    while (!ready()) {
        QApplication::processEvents(QEventLoop::AllEvents, 50);
        require(timer.elapsed() < ms, "Qt operation timed out");
        QThread::msleep(10);
    }
}
class Reply : public QNetworkReply {
    QBuffer buffer;
public:
    Reply(const QNetworkRequest &request, QHelpEngine &engine, QObject *parent)
        : QNetworkReply(parent) {
        setRequest(request); setUrl(request.url());
        const auto bytes = request.url().scheme() == "qthelp" ? engine.fileData(request.url()) : QByteArray();
        if (bytes.isEmpty()) setError(ContentNotFoundError, "Offline or absent resource");
        buffer.setData(bytes); buffer.open(QIODevice::ReadOnly); open(QIODevice::ReadOnly);
        QTimer::singleShot(0, this, [this]() { setFinished(true); emit readyRead(); emit finished(); });
    }
    void abort() override {}
    qint64 bytesAvailable() const override { return buffer.bytesAvailable()+QNetworkReply::bytesAvailable(); }
    qint64 readData(char *data, qint64 max) override { return buffer.read(data, max); }
};
class Network : public QNetworkAccessManager {
    QHelpEngine &engine;
public:
    Network(QHelpEngine &engine, QObject *parent): QNetworkAccessManager(parent), engine(engine) {}
    QNetworkReply *createRequest(Operation op, const QNetworkRequest &request, QIODevice *data) override {
        if (request.url().scheme() == "data") return QNetworkAccessManager::createRequest(op, request, data);
        return new Reply(request, engine, this);
    }
};
int main(int argc, char **argv) {
    QApplication app(argc, argv);
    try {
        require(argc == 3, "Usage: qt_compat DISPOSABLE_HELP_DIRECTORY EVIDENCE_DIRECTORY");
        QDir help(argv[1]), out(argv[2]);
        QFile qch(help.absoluteFilePath("gauss.qch"));
        require(qch.open(QIODevice::ReadOnly), "Cannot read QCH");
        auto qchHash = QCryptographicHash::hash(qch.readAll(), QCryptographicHash::Sha256).toHex();
        QHelpEngine engine(help.absoluteFilePath("gauss.qhc"));
        require(engine.setupData(), "Collection setup failed");
        auto names = engine.registeredDocumentations();
        require(names.size() == 1, "Unexpected namespace count");
        require(!engine.linksForIdentifier("ols").isEmpty(), "OLS context help missing");
        require(!engine.fileData(QUrl("qthelp://aptech.com.gauss.26.0/doc/welcome.html")).isEmpty(), "Application home fallback failed");
        require(!engine.fileData(QUrl("qthelp://aptech.com.gauss.27.0/doc/welcome.html")).isEmpty(), "GAUSS 27 home fallback failed");
        QJsonObject result{{"qt_version", qVersion()}, {"namespace", names.first()}, {"application_home_resolves", true}, {"qch_sha256", QString(qchHash)}};
        bool indexed = false;
        auto search = engine.searchEngine();
        QObject::connect(search, &QHelpSearchEngine::indexingFinished, [&]() { indexed = true; });
        search->reindexDocumentation(); until([&]() { return indexed; });
        int found = -1;
        QObject::connect(search, &QHelpSearchEngine::searchingFinished, [&](int n) { found = n; });
        search->search("regression"); until([&]() { return found >= 0; });
        require(found > 0, "Full text search failed");
        result["search_results_regression"] = found;
        QWebView view;
        view.resize(1100, 850); view.page()->setNetworkAccessManager(new Network(engine, &view));
        view.show();
        QJsonArray pages;
        for (const auto &name : {"welcome.html", "ols.html", "cdfncdfnc.html", "IN-Introduction.html", "plotxy.html", "changelog.html", "minimize.html", "tsaggregate.html"}) {
            bool loaded = false, okay = false;
            auto connection = QObject::connect(&view, &QWebView::loadFinished, [&](bool ok) { loaded = true; okay = ok; });
            view.load(QUrl("qthelp://"+names.first()+"/doc/"+name));
            until([&]() { return loaded; }); require(okay, "Rendering page failed");
            auto frame = view.page()->mainFrame();
            require(frame->toPlainText().size() > 200, "Empty page");
            if (QString(name) == "cdfncdfnc.html" || QString(name) == "ols.html") {
                frame->evaluateJavaScript("window.mathDone=false; if(window.MathJax && MathJax.Hub) MathJax.Hub.Queue(function(){window.mathDone=true;});");
                until([&]() { return frame->evaluateJavaScript("window.mathDone === true").toBool(); }, 60000);
            }
            int math = frame->evaluateJavaScript("document.querySelectorAll('.MathJax, .MathJax_Display').length").toInt();
            if (QString(name) == "cdfncdfnc.html") require(math > 0, "Math rendering failed");
            int images = frame->evaluateJavaScript("Array.prototype.filter.call(document.images, function(i){return i.complete && i.naturalWidth>0;}).length").toInt();
            if (QString(name) == "plotxy.html") {
                require(images > 0, "Plot image did not render");
                frame->evaluateJavaScript("document.images[0].scrollIntoView()");
            }
            if (QString(name) == "minimize.html" || QString(name) == "tsaggregate.html")
                frame->evaluateJavaScript("document.getElementById('format').scrollIntoView()");
            QImage image(view.size(), QImage::Format_ARGB32); image.fill(Qt::white);
            QPainter painter(&image); frame->render(&painter); painter.end();
            require(image.save(out.absoluteFilePath(QString("qt-native-")+name+".png")), "Screenshot save failed");
            pages.append(QJsonObject{{"page", name}, {"text_characters", frame->toPlainText().size()}, {"math_elements", math}, {"loaded_images", images}});
            QObject::disconnect(connection);
        }
        result["pages"] = pages;
        QFile file(out.absoluteFilePath("qt-native-validation.json"));
        require(file.open(QIODevice::WriteOnly), "Cannot save result");
        file.write(QJsonDocument(result).toJson());
        return 0;
    } catch (const std::exception &error) {
        qCritical("%s", error.what()); return 1;
    }
}
