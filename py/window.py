#!/usr/bin/env python3

import sys
import random
from PyQt5 import QtWidgets, QtCore, QtGui


class TegenBoard(QtWidgets.QWidget):
    """
    Tegen board widget. Currently has the Tegen grid.
    Inherits from QWidget
    Nothing here is for external use.
    
    Overwritten or new methods:
    void init_ui(): defines and draws the widget
    void paintEvent(QPaintEvent e): redraws the widget on each paint event
    void resizeEvent(QResizeEvent e): redefines the grid when widget is
                                      resized and queues it to be redrawn
    void keyPressEvent(QKeyEvent e): When a key is pressed, sets a single tile
                                     to a random color. The tile that is
                                     recolored is determined by taking the
                                     modulo of the keycode and the number of
                                     tiles.

    Instance variables:
    dict tiles[] = {"rect": QRect, "color": QColor, "image": QImage}:
        List of arrays in the described form. Keys are as follows:
        QRect rect: defines the object to paint. Initially set by init_ui, and
                    updated by resizeEvent()
        QColor color: the fill color. Initially set by init_ui() to
                      QColor(255, 255, 255), and updated to a random color by
                      keyPressEvent.
        QImage image: Initially set to None. Should this be set to an actual
                      value, it will be painted on the tile.
    """
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Tegen")

        self.tiles = []

        for i in range(7):
            for j in range(7):
                if abs(i - 3) + abs(j - 3) >= 5:
                    continue


                self.tiles.append({"rect": QtCore.QRect((self.width() / 7) * i,
                    (self.height() / 7) * j, self.width() / 7 - 1,
                    self.height() / 7 - 1),
                    "color": QtGui.QColor(255,255,255),
                    "image": None
                })

        self.show()

    def paintEvent(self, e):
        painter = QtGui.QPainter(self)
        painter.setPen(QtGui.QColor(0,0,0))
        for i in range(len(self.tiles)):
            painter.drawRect(self.tiles[i]["rect"])
            painter.fillRect(self.tiles[i]["rect"], self.tiles[i]["color"])
            if self.tiles[i]["image"]:
                painter.drawImage(self.tiles[i]["rect"], self.tiles[i]["image"])


    def resizeEvent(self, e):
        idx = 0

        for i in range(7):
            for j in range(7):
                if abs(i - 3) + abs(j - 3) >= 5:
                    continue

                self.tiles[idx]["rect"].setRect((self.width() / 7) * i,
                    (self.height() / 7) * j, self.width() / 7 - 1,
                    self.height() / 7 - 1)

                idx += 1

        self.update()

    def keyPressEvent(self, e):
        self.tiles[e.key() % len(self.tiles)]["color"] = QtGui.QColor(
            *[random.randint(0,255) for i in range(3)])

        self.repaint(self.tiles[e.key() % len(self.tiles)]["rect"])


def main():
    app = QtWidgets.QApplication(sys.argv)
    board = TegenBoard()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
