FROM docker.io/library/python:3.10.16-slim-bookworm@sha256:5fb1a18941b20a1be253974bf5ad9e63c9e251279856649b356178962e8908a2

# Fixed Debian snapshot pins the complete native dependency closure. Network is
# needed only while preparing this image, never while generating help.
RUN rm -f /etc/apt/sources.list.d/debian.sources && \
    printf 'deb [check-valid-until=no] https://snapshot.debian.org/archive/debian/20250301T000000Z bookworm main\n' > /etc/apt/sources.list && \
    apt-get update && apt-get install -y --no-install-recommends \
      qttools5-dev-tools python3-pyqt5 python3-pyqt5.qtwebkit \
      libqt5sql5-sqlite fonts-dejavu-core && \
    dpkg-query -W > /opt/native-packages.lock && rm -rf /var/lib/apt/lists/*
COPY requirements.lock /opt/requirements.lock
# Archive uses docutils 0.18.1 despite Sphinx 3.4.3's older declared upper
# bound. The complete closure is explicit and matches archive docutils.
RUN pip install --no-cache-dir --no-deps --require-hashes -r /opt/requirements.lock && \
    pip freeze > /opt/python-packages.lock
COPY generate.py html_build.py inputs.py validate.py qt_probe.py runner.py /opt/app-help/
COPY app-help.css /opt/app-help/app-help.css
ENV QT_QPA_PLATFORM=offscreen PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /scratch
ENTRYPOINT ["python", "/opt/app-help/runner.py"]
