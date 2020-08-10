from PySide2 import QtWidgets
from .weather_ui import WeatherUi
import _thread


class Index(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 600, 800)
        self.setWindowTitle('天气预报系统')

        self.button = QtWidgets.QPushButton("天气预报", self)
        self.button.setGeometry(200, 200, 200, 200)
        self.text = QtWidgets.QLabel("Hello World")

        self.button.clicked.connect(self.open_weather_window)

        # other UI
        self.weather_window = WeatherUi()

    def open_weather_window(self):
        self.weather_window.show()
        self.close()
