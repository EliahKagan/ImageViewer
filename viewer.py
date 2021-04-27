import argparse
import math
import os
import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

parser = argparse.ArgumentParser('Image Viewer')
parser.add_argument('path',
                    nargs='?',
                    help='The path of the image to be opened.',
                    type=str)
path = parser.parse_args().path

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Image Viewer')

screenBounds = app.desktop().screenGeometry(window)
maxWidth = math.floor(screenBounds.width() * 0.9)
maxHeight = math.floor(screenBounds.height() * 0.9)

if path is None:
    path, _ = QFileDialog.getOpenFileName(window,
                                          'Open Image File',
                                          r'D:\Downloads')
    if not path:
        sys.exit(1)

picture = QPixmap(path)
if picture.width() > maxWidth or picture.height() > maxHeight:
    picture = picture.scaled(maxWidth, maxHeight, Qt.KeepAspectRatio)

label = QLabel(window)
label.setPixmap(picture)
label.setGeometry(0, 0, picture.width(), picture.height())

window.resize(picture.width(), picture.height())
window.show()
sys.exit(app.exec_())
