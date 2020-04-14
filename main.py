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

        self.rotateplus = QPushButton('Повернуть направо', self)
        self.rotateplus.setGeometry(10, 10, 160, 40)
        self.rotateplus.clicked.connect(self.rotate)
        self.rotatemin = QPushButton('Повернуть налево', self)
        self.rotatemin.setGeometry(230, 10, 160, 40)
        self.rotatemin.clicked.connect(self.rotate)
        self.r = QPushButton('R', self)
        self.g = QPushButton('G', self)
        self.b = QPushButton('B', self)
        self.r.setGeometry(10, 60, 50, 50)
        self.g.setGeometry(70, 60, 50, 50)
        self.b.setGeometry(130, 60, 50, 50)
        self.r.clicked.connect(self.onClick)
        self.g.clicked.connect(self.onClick)
        self.b.clicked.connect(self.onClick)

        self.noup = QPushButton('ГДЕ МОИ ЦВЕТА?', self)
        self.noup.setGeometry(190, 60, 200, 50)
        self.noup.clicked.connect(self.onClick)

    def rotate(self):
        try:
            im = Image.open(self.image)
            if self.sender().text() == 'Повернуть направо':
                rot = -90
            else:
                rot = 90
            im1 = im.rotate(rot, expand=True)
            im1.save('imagene.jpg')
            self.draw.load('imagene.jpg')
            self.image = 'imagene.jpg'
            self.image1.setPixmap(self.draw)
        except Exception as e:
            print('error in rotate(), stack:', e)

    def onClick(self):
        try:
            im = Image.open('main_image.png')
            x, y = im.size
            pix = im.load()
            for i in range(x):
                for j in range(y):
                    r, g, b = pix[i, j]
                    if self.sender().text() == 'R':
                        pix[i, j] = r, 0, 0
                    elif self.sender().text() == 'G':
                        pix[i, j] = 0, g, 0
                    elif self.sender().text() == 'B':
                        pix[i, j] = 0, 0, b
                    else:
                        pass

            im.save('imagene.jpg')
            self.draw.load('imagene.jpg')
            self.image = 'imagene.jpg'
            self.image1.setPixmap(self.draw)
        except Exception as e:
            print('error in onClick(), stack:', e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
