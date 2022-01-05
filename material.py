import matplotlib.pyplot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

from PyQt5.QtWidgets import *


class Alignments:
    Start = 0
    Center = 1
    End = 2
    SpaceAround = 3


class Color:
    def __init__(self, hex_color: hex):
        if hex_color > 0xFFFFFF or hex_color < 0x000000:
            raise ValueError("hex_color has to be between 0x000000 and 0xFFFFFF")
        self.__hex = hex_color

    @property
    def rgb(self):
        return self.__hex // 0x00FFFF, self.__hex % 0x010000 // 0x0000FF, self.__hex % 0x000100

    @property
    def hex(self):
        return hex(self.__hex)


class Colors:
    RED = Color(0xFF0000)
    GREEN = Color(0x00FF00)
    BLUE = Color(0x0000FF)
    WHITE = Color(0xFFFFFF)
    BLACK = Color(0x000000)


class Widgets:
    class Row(QWidget):
        def __init__(self,
                     children: list[QWidget],
                     alignment: Alignments.Start | Alignments.Center | Alignments.End = Alignments.SpaceAround):
            super().__init__()
            layout = QHBoxLayout()
            if alignment is Alignments.End:
                layout.addStretch()

            for child in children:
                layout.addWidget(child)

            if alignment is Alignments.Start:
                layout.addStretch()

            self.setLayout(layout)

    class Column(QWidget):
        def __init__(self,
                     children: list[QWidget],
                     alignment: Alignments.Start | Alignments.Center | Alignments.End = Alignments.SpaceAround):
            super().__init__()
            layout = QVBoxLayout()
            if alignment is Alignments.End:
                layout.addStretch()

            for child in children:
                layout.addWidget(child)

            if alignment is Alignments.Start:
                layout.addStretch()

            self.setLayout(layout)

    class Button(QPushButton):
        def __init__(self, text: str, on_tap=None):
            super().__init__()
            self.setText(text)
            if on_tap is not None:
                self.clicked.connect(on_tap)

    class TextField(QLineEdit):
        def __init__(self, init_text=""):
            super().__init__()
            self.setText(init_text)

    class Text(QLabel):
        def __init__(self, text: str):
            super().__init__()
            self.setText(text)

    class PyPlotImage(FigureCanvasQTAgg):
        def __init__(self, figure: matplotlib.pyplot.figure):
            super().__init__(figure)

    class Table(QWidget):
        def __init__(self, children: list[QWidget], x_size: int = None, y_size: int = None, horizontal_filling=True,
                     spacing: int = 0):
            super().__init__()
            layout = QGridLayout()

            if horizontal_filling:
                if x_size is None:
                    raise ValueError("When table is filling in HORIZONTAL, X_SIZE has to be defined.")
                for index, child in enumerate(children):
                    x = index % x_size
                    y = index // x_size
                    if y_size is not None and y >= y_size:
                        break
                    layout.addWidget(child, y, x)
            else:
                if y_size is None:
                    raise ValueError("When table is filling in VERTICAL, Y_SIZE has to be defined.")
                for index, child in enumerate(children):
                    y = index % y_size
                    x = index // y_size
                    if x_size is not None and x >= x_size:
                        break
                    layout.addWidget(child, y, x)

            layout.setSpacing(spacing)
            self.setLayout(layout)

    class Container(QLabel):
        def __init__(self, child: QWidget = None, color: Color = None, height: int = None, width: int = None):
            super().__init__()
            if child is not None:
                layout = QHBoxLayout()
                layout.addWidget(child)
                self.setLayout(layout)
            styleSheet = ""
            if color is not None:
                styleSheet += f"background-color: #{str(color.hex)[2:]};"
            if height is not None:
                self.geometry().setHeight(height)
            if width is not None:
                self.geometry().setWidth(width)
            self.setStyleSheet(styleSheet)
