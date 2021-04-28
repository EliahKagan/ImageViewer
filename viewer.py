import argparse
import math
import os
import sys

from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import (QApplication,
                               QFileDialog,
                               QLabel,
                               QMessageBox,
                               QWidget)

APP_NAME = 'Image Viewer'
MAX_START_RATIO = 0.9

RSQUO = '\N{RIGHT SINGLE QUOTATION MARK}'
LDQUO = '\N{LEFT DOUBLE QUOTATION MARK}'
RDQUO = '\N{RIGHT DOUBLE QUOTATION MARK}'

parser = argparse.ArgumentParser(APP_NAME)
parser.add_argument('path',
                    nargs='?',
                    help='The path of the image to be opened.',
                    type=str)
path = parser.parse_args().path

print(f'{sys.argv[0]}: PID {os.getpid()}', file=sys.stderr)

app = QApplication(sys.argv)
window = QWidget()
screenBounds = app.desktop().screenGeometry(window)
maxWidth = math.floor(screenBounds.width() * MAX_START_RATIO)
maxHeight = math.floor(screenBounds.height() * MAX_START_RATIO)

if path is None:
    path, _ = QFileDialog.getOpenFileName(window,
                                          'Open Image File',
                                          os.path.expanduser('~'))
    if not path:
        sys.exit(1)  # If the user cancels out of the dialog, just quit.

picture = QPixmap(path)

if picture.isNull():
    dialog = QMessageBox(window)
    dialog.setWindowTitle(window.windowTitle())
    dialog.setText(f'Couldn{RSQUO}t open {LDQUO}{path}{RDQUO}')
    dialog.setWindowFlag(Qt.WindowStaysOnTopHint)
    dialog.exec_()
    sys.exit(1)

if picture.width() > maxWidth or picture.height() > maxHeight:
    picture = picture.scaled(maxWidth, maxHeight, Qt.KeepAspectRatio)

label = QLabel(window)
label.setPixmap(picture)
label.setGeometry(0, 0, picture.width(), picture.height())

window.setWindowTitle(f'{APP_NAME} - {os.path.basename(path)}')
window.resize(picture.width(), picture.height())
window.show()
sys.exit(app.exec_())
