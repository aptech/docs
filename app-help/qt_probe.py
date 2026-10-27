"""Use Qt Help, full-text search, and the Qt WebKit renderer used by GAUSS."""
import json
import sys
import time
from pathlib import Path
from PyQt5.QtCore import QBuffer, QByteArray, QEventLoop, QIODevice, QTimer, QUrl, QT_VERSION_STR
from PyQt5.QtGui import QPainter, QImage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtHelp import QHelpEngine
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest
from PyQt5.QtWebKitWidgets import QWebView

app = QApplication(sys.argv)
directory, output = map(Path, sys.argv[1:3])
engine = QHelpEngine(str(directory/'gauss.qhc'))
assert engine.setupData(), engine.error()
ns = engine.registeredDocumentations()[0]
assert engine.linksForIdentifier('ols'), 'Context identifier ols unavailable'
report = {'qt_version': QT_VERSION_STR, 'namespace': ns, 'pages': {}, 'requests_failed': []}

def wait_until(predicate, seconds=60):
    deadline = time.monotonic()+seconds
    while not predicate():
        app.processEvents(QEventLoop.AllEvents, 50)
        if time.monotonic() > deadline:
            raise TimeoutError('Qt operation exceeded '+str(seconds)+' seconds')
        time.sleep(.01)

search = engine.searchEngine()
indexed = []
search.indexingFinished.connect(lambda: indexed.append(True))
search.reindexDocumentation()
wait_until(lambda: indexed, 120)
searched = []
search.searchingFinished.connect(lambda n: searched.append(n))
search.search('regression')
wait_until(lambda: searched)
assert searched[0] > 0, 'No full text search results'
report['search_results_regression'] = searched[0]

class Reply(QNetworkReply):
    def __init__(self, request, parent):
        super().__init__(parent)
        self.setRequest(request)
        self.setUrl(request.url())
        self.buf = QBuffer(self)
        data = engine.fileData(request.url()) if request.url().scheme() == 'qthelp' else QByteArray()
        if not data:
            report['requests_failed'].append(request.url().toString())
            self.setError(QNetworkReply.ContentNotFoundError, 'Resource unavailable/offline')
        self.buf.setData(data)
        self.buf.open(QIODevice.ReadOnly)
        self.open(QIODevice.ReadOnly)
        QTimer.singleShot(0, self.done)
    def done(self):
        self.setFinished(True)
        self.readyRead.emit()
        self.finished.emit()
    def readData(self, size):
        return bytes(self.buf.read(size))
    def bytesAvailable(self):
        return self.buf.bytesAvailable()+super().bytesAvailable()
    def abort(self):
        pass

class Network(QNetworkAccessManager):
    def createRequest(self, operation, request, outgoing=None):
        if request.url().scheme() == 'data':
            return super().createRequest(operation, request, outgoing)
        return Reply(request, self)

view = QWebView()
view.resize(1100, 850)
network = Network(view)
view.page().setNetworkAccessManager(network)
view.show()
for name in ['welcome.html', 'ols.html', 'cdfncdfnc.html', 'IN-Introduction.html', 'plotxy.html']:
    loaded = []
    def done(ok):
        loaded.append(ok)
    view.loadFinished.connect(done)
    view.load(QUrl('qthelp://'+ns+'/doc/'+name))
    wait_until(lambda: loaded)
    assert loaded[0], name
    frame = view.page().mainFrame()
    if name in ('ols.html', 'cdfncdfnc.html'):
        frame.evaluateJavaScript('window.mathDone=false; if(window.MathJax && MathJax.Hub) MathJax.Hub.Queue(function(){window.mathDone=true;});')
        wait_until(lambda: frame.evaluateJavaScript('window.mathDone === true'))
    text = frame.toPlainText()
    assert len(text) > 200, name
    images = frame.evaluateJavaScript('Array.prototype.filter.call(document.images, function(i){return i.complete && i.naturalWidth>0;}).length')
    if name == 'plotxy.html':
        assert images > 0, 'Plot image did not render'
        frame.evaluateJavaScript('document.images[0].scrollIntoView()')
    png = output/(name+'.png')
    img = QImage(view.size(), QImage.Format_ARGB32)
    img.fill(0xffffffff)
    painter = QPainter(img)
    frame.render(painter)
    painter.end()
    assert img.save(str(png))
    report['pages'][name] = {'text_characters': len(text),
        'loaded_images': images,
        'math_elements': frame.evaluateJavaScript('document.querySelectorAll(".MathJax, .MathJax_Display").length'),
        'screenshot': png.name}
    view.loadFinished.disconnect(done)
# GAUSS sets this differently from the packager namespace. Verify Qt's fallback.
home = QUrl('qthelp://aptech.com.gauss.26.0/doc/welcome.html')
report['application_home_resolved'] = engine.findFile(home).toString()
assert engine.fileData(home), 'GAUSS home URL does not resolve'
(output/'qt-validation.json').write_text(json.dumps(report, indent=2))
assert report['pages']['cdfncdfnc.html']['math_elements'] > 0, 'No rendered math'
print(json.dumps(report, indent=2))
