import sys
from PySide2 import QtWidgets
from locations.deal_load_locs import deal_loc_dic
from ui import index


if __name__ == '__main__':
    deal_loc_dic()
    app = QtWidgets.QApplication([])
    widget = index.Index()
    widget.show()
    sys.exit(app.exec_())
