import sys
import os
import signal

from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine, QQmlContext
from PyQt6.QtCore import Qt, QObject, pyqtProperty

from SensorManager import SensorManager

class PixelDash(QObject):
    def __init__(self):
        QObject.__init__(self)
        self._sensorManager = None

    def stop(self):
        if self._sensorManager:
            self._sensorManager.stop()

    @pyqtProperty(QObject, constant=True)
    def sensors(self) -> SensorManager:
        if not self._sensorManager:
            self._sensorManager = SensorManager()
        return self._sensorManager

    @pyqtProperty(str, constant=True)
    def test(self) -> str:
        return "hello world!"


if __name__ == "__main__":
    # Unify default control looks across platforms
    os.environ["QT_QUICK_CONTROLS_STYLE"] = "Fusion"

    # Create an instance of the application
    app = QGuiApplication(sys.argv)

    # Hide the cursor
    if False:
        app.setOverrideCursor(Qt.CursorShape.BlankCursor);

    pixelDash = PixelDash()

    # Create QML engine
    engine = QQmlApplicationEngine()
    context = QQmlContext(engine.rootContext()) #type: ignore #MyPy doens't realise that engine can't be None here.

    engine.rootContext().setContextProperty("app", pixelDash)
    engine.load(os.path.join("resources", "qml", "PixelDash.qml"))

    # Catch CTRL+C and close the app when the window is closed
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    engine.quit.connect(app.quit)

    result = app.exec()
    pixelDash.stop()
    sys.exit(result)