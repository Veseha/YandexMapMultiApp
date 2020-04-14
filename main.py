from PyQt5.QtWidgets import QApplication, QWidget, QShortcut
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QPixmap, QImage, QKeySequence
import sys
from geocoderAPI import get_cords
from mapsAPI import get_image
from PIL import Image
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QFileDialog, QLineEdit, QLabel, QTextEdit

# ------------------------ global variable -------------------------

actual_cords = [0, 0]
zoom = 9
lmap = 'map'
SCREEN_SIZE = [600, 550]

# ------------------------------ func -----------------------------


def upd_map():
    get_image(actual_cords[0], actual_cords[1], zoom=zoom, l=lmap)


def get_image_from_toponym(req):
    global actual_cords
    actual_cords = get_cords(req)
    get_image(actual_cords[0], actual_cords[1], zoom=zoom, l=lmap)


get_image_from_toponym(input())


# -------------------------- pyqt ----------------------------

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.image = 'main_image.png'
        self.initUI()

    def initUI(self):
        self.move(400, 400)
        self.setFixedSize(*SCREEN_SIZE)
        self.setWindowTitle('Отображение картинки')
        self.draw = QPixmap(self.image)
        self.image1 = QLabel(self)
        self.image1.move(0, 100)
        self.image1.resize(600, 450)
        self.image1.setPixmap(self.draw)

        self.searchbar = QTextEdit(self)
        self.searchbar.setAcceptRichText(False)
        self.searchbar.setGeometry(0, 0, 250, 50)

        self.searchbutton = QPushButton(self, text='search')
        self.searchbutton.setGeometry(250, 0, 60, 25)
        self.searchbutton.action = 'start_search'
        self.searchbutton.clicked.connect(self.onClick)

        key_enter = QShortcut(QKeySequence('enter'), self)
        key_enter.action = 'search'
        key_enter.activated.connect(self.onClick)

        self.zoomup = QPushButton(self, text='+')
        self.zoomup.setGeometry(250, 25, 30, 25)
        self.zoomup.action = 'zoomplus'
        self.zoomup.clicked.connect(self.onClick)

        key_pageup = QShortcut(QKeySequence('PgUp'), self)
        key_pageup.action = 'zoomplus'
        key_pageup.activated.connect(self.onClick)

        self.zoomdown = QPushButton(self, text='-')
        self.zoomdown.setGeometry(280, 25, 30, 25)
        self.zoomdown.action = 'zoomminus'
        self.zoomdown.clicked.connect(self.onClick)

        self.map1 = QPushButton(self, text='map')
        self.map1.setGeometry(310, 0, 30, 25)
        self.map1.action = 'map'
        self.map1.clicked.connect(self.onClick)

        self.map2 = QPushButton(self, text='sat')
        self.map2.setGeometry(310, 25, 30, 25)
        self.map2.action = 'sat'
        self.map2.clicked.connect(self.onClick)

        self.map3 = QPushButton(self, text='skl')
        self.map3.setGeometry(340, 0, 30, 25)
        self.map3.action = 'skl'
        self.map3.clicked.connect(self.onClick)

        self.map4 = QPushButton(self, text='trf')
        self.map4.setGeometry(340, 25, 30, 25)
        self.map4.action = 'trf'
        self.map4.clicked.connect(self.onClick)

        key_pagedown = QShortcut(QKeySequence('PgDown'), self)
        key_pagedown.action = 'zoomminus'
        key_pagedown.activated.connect(self.onClick)

    def updateUI(self):
        self.draw = QPixmap(self.image)
        self.image1.setPixmap(self.draw)

    def onClick(self):
        global zoom, actual_cords, lmap
        try:
            print('zoom is', zoom, 'cords are', actual_cords)
            if self.sender().action == 'start_search':
                get_image_from_toponym(self.searchbar.toPlainText())
                self.updateUI()
            if self.sender().action == 'zoomplus':
                if zoom < 18:
                    zoom += 1
                    upd_map()

            if self.sender().action == 'zoomminus':
                if zoom > 4:
                    zoom -= 1
                    upd_map()
            if self.sender().action == 'map':
                lmap = 'map'
                upd_map()
            if self.sender().action == 'sat':
                lmap = 'sat'
                upd_map()
            if self.sender().action == 'skl':
                lmap = 'skl'
                upd_map()
            if self.sender().action == 'trf':
                lmap = 'trf'
                upd_map()

            self.updateUI()
        except Exception as e:
            print('error in onClick(), stack:', e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
