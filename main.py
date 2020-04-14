from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QPixmap, QImage
import sys
from geocoderAPI import get_cords
from mapsAPI import get_image
from PIL import Image
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QFileDialog, QLineEdit, QLabel, QTextEdit


def get_image_from_cords(req):
    res = get_cords(req)
    get_image(res[0], res[1])


get_image_from_cords(input('Input your adress'))

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
        self.image1.resize(350, 350)
        self.image1.setPixmap(self.draw)

    def onClick(self):
        try:
            pass
        except Exception as e:
            print('error in onClick(), stack:', e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
