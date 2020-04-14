from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QPixmap, QImage
import sys
from geocoderAPI import get_cords
from mapsAPI import get_image
from PIL import Image
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QFileDialog, QLineEdit, QLabel, QTextEdit


actual_cords = [0, 0]
zoom = 9

def get_image_from_toponym(req):
    global actual_cords
    actual_cords = get_cords(req)
    get_image(actual_cords[0], actual_cords[1], zoom=zoom)


SCREEN_SIZE = [400, 500]


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.image = 'main_image.png'
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, *SCREEN_SIZE)
        self.setWindowTitle('Отображение картинки')
        self.draw = QPixmap(self.image)
        self.image1 = QLabel(self)
        self.image1.move(10, 100)
        self.image1.resize(400, 400)
        self.image1.setPixmap(self.draw)

        self.searchbar = QTextEdit(self)
        self.searchbar.setGeometry(0, 0, 250, 60)

        self.searchbutton = QPushButton(self, text='search')
        self.searchbutton.setGeometry(250, 0, 60, 25)
        self.searchbutton.action = 'start_search'
        self.searchbutton.clicked.connect(self.onClick)

        self.zoomup = QPushButton(self, text='Z+')
        self.zoomup.setGeometry(300, 0, 40, 40)
        self.zoomup.action = 'zoomplus'
        self.zoomup.clicked.connect(self.onClick)


        self.zoomdown = QPushButton(self, text='Z-')
        self.zoomdown.setGeometry(340, 0, 40, 40)
        self.zoomdown.action = 'zoomminus'
        self.zoomdown.clicked.connect(self.onClick)



    def updateUI(self):
        self.draw = QPixmap(self.image)
        self.image1.setPixmap(self.draw)

    def onClick(self):
        global zoom, actual_cords
        try:
            if self.sender().action == 'start_search':
                get_image_from_toponym(self.searchbar.toPlainText())
                self.updateUI()
            if self.sender().action == 'zoomplus':
                if zoom < 13:
                    zoom += 1
                    get_image(actual_cords[0], actual_cords[1], zoom=zoom)
                    print(zoom)
                    self.updateUI()

            if self.sender().action == 'zoomminus':
                if zoom > 4:
                    zoom -= 1
                    get_image(actual_cords[0], actual_cords[1], zoom=zoom)
                    print(zoom)
                    self.updateUI()

        except Exception as e:
            print('error in onClick(), stack:', e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
