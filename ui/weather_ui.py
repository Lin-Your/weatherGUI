from PySide2 import QtWidgets
from PySide2.QtCore import QRect, Qt
import json
import _thread
from spd import spider
from locations.deal_load_locs import load_locations_info


class WeatherUi(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 900, 600)
        self.setFixedSize(900, 600)
        self.setWindowTitle('Weather forest')

        self.textBox = QtWidgets.QTextEdit(self)
        self.textBox.setGeometry(100, 100, 400, 400)

        # HorizontalLayout0
        self.hLayoutWidget0 = QtWidgets.QWidget(self)
        self.hLayoutWidget0.setGeometry(QRect(530, 95, 330, 30))
        self.hLayout0 = QtWidgets.QHBoxLayout(self.hLayoutWidget0)
        self.hLayout0.setContentsMargins(0, 0, 0, 0)
        # HorizontalLayout1
        self.hLayoutWidget1 = QtWidgets.QWidget(self)
        self.hLayoutWidget1.setGeometry(QRect(530, 125, 330, 300))
        self.hLayout1 = QtWidgets.QHBoxLayout(self.hLayoutWidget1)
        self.hLayout1.setContentsMargins(0, 0, 0, 0)

        # 3 Labels and ListView to show cities
        self.labels = []
        self.listWidgets = []
        tips = [r'省级行政区', r'地级行政区', r'县级行政区']

        for _ in range(3):
            tp = QtWidgets.QLabel(text=tips[_])
            tp.setAlignment(Qt.AlignCenter)
            self.hLayout0.addWidget(tp)
            self.labels.append(tp)

            tp = QtWidgets.QListWidget(self.hLayoutWidget1)
            self.hLayout1.addWidget(tp, Qt.AlignCenter)
            self.listWidgets.append(tp)

        self.locations_info = load_locations_info()
        for province in self.locations_info.keys():
            self.listWidgets[0].addItem(province)
        self.listWidgets[0].currentItemChanged.connect(lambda: self.load_list_widgets(0))
        self.listWidgets[1].currentItemChanged.connect(lambda: self.load_list_widgets(1))
        self.listWidgets[0].setCurrentRow(0)

        # GridLayout1
        self.gLayoutWidget = QtWidgets.QWidget(self)
        self.gLayoutWidget.setGeometry(QRect(550, 420, 300, 100))
        self.gLayout = QtWidgets.QGridLayout(self.gLayoutWidget)

        # Click Button to get weather metadata
        self.clickBtn = QtWidgets.QPushButton('获取', self)
        self.clickBtn.clicked.connect(self.change)
        # 4 RadioButton to select mode
        self.radioBtn0 = QtWidgets.QRadioButton('现在', self)
        self.radioBtn1 = QtWidgets.QRadioButton('3天', self)
        self.radioBtn2 = QtWidgets.QRadioButton('7天', self)
        self.radioBtn3 = QtWidgets.QRadioButton('24小时', self)
        # default checked
        self.radioBtn0.setChecked(True)

        # Buttons' location in GridLayout1
        self.gLayout.addWidget(self.radioBtn0, 0, 0, 1, 1, Qt.AlignHCenter)
        self.gLayout.addWidget(self.radioBtn1, 0, 1, 1, 1, Qt.AlignHCenter)
        self.gLayout.addWidget(self.radioBtn2, 0, 2, 1, 1, Qt.AlignHCenter)
        self.gLayout.addWidget(self.radioBtn3, 0, 3, 1, 1, Qt.AlignHCenter)
        self.gLayout.addWidget(self.clickBtn, 1, 1, 1, 2, Qt.AlignHCenter)

        self.Spider = spider.Spider()

    def load_list_widgets(self, flag: int):
        """
        将城市列表加载到ListWidgets中
        """
        if not flag:
            self.listWidgets[1].clear()
            province = self.listWidgets[0].currentItem().text()
            cities = self.locations_info[province].keys()
            self.listWidgets[1].addItems(cities)
            self.listWidgets[1].setCurrentRow(0)
        elif self.listWidgets[1].currentItem():
            self.listWidgets[2].clear()
            _province = self.listWidgets[0].currentItem().text()
            _city = self.listWidgets[1].currentItem().text()
            locations = self.locations_info[_province][_city].keys()
            self.listWidgets[2].addItems(locations)
            self.listWidgets[2].setCurrentRow(0)

    def change_list_widgets(self):
        pass

    def change(self):
        if self.radioBtn1.isChecked():
            mode = 'daily-3'
        elif self.radioBtn2.isChecked():
            mode = 'daily-7'
        elif self.radioBtn3.isChecked():
            mode = 'hourly'
        else:  # default mode
            mode = 'now'
        n1 = self.listWidgets[0].currentItem().text()
        n2 = self.listWidgets[1].currentItem().text()
        n3 = self.listWidgets[2].currentItem().text()
        city_id = self.locations_info[n1][n2][n3]
        metadata = self.Spider.get_data(city_id, 'weather', mode)
        if not metadata:
            return
        # metadata = self.data_cleaning(metadata, mode.split('-')[0])
        metadata = json.dumps(metadata, indent=4, ensure_ascii=False)
        self.textBox.setText(metadata)

    def data_cleaning(self, metadata: dict, mode: str):
        update_time = metadata['updateTime']
        mdt = metadata[mode]
        if mode == 'now':
            pass
        else:
            pass
        dt = ''
        return dt
