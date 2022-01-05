import sys

import numpy

from functions import Functions
from material import *


class UI1:
    TITLE = "Stat"
    WIDTH = 1500
    HEIGHT = 600

    def __init__(self):
        self._app = QApplication(sys.argv)

        self._intervals_count = 20
        self._name_field = Widgets.TextField(init_text="input.xlsx")
        self.__data: numpy.ndarray = numpy.random.random((100, 2))
        self.__build()

    def __build(self):
        sorted_data = Functions.sort_np_data(self.__data).T
        normalized_data = numpy.array([Functions.normalize(sorted_data[0]), Functions.normalize(sorted_data[1])])
        self._window = Widgets.Row(children=[
            Widgets.Table(x_size=2,
                          children=[
                              Widgets.PyPlotImage(Functions.get_scatter(*self.__data.T, title="Входные данные")),
                              Widgets.PyPlotImage(Functions.get_two_plots(*normalized_data,
                                                                          title="Нормализованные данные")),
                              Widgets.PyPlotImage(Functions.get_intervals(self.__data.T[0], self._intervals_count,
                                                                          title="Нормальное распределение A")),
                              Widgets.PyPlotImage(Functions.get_intervals(self.__data.T[1], self._intervals_count,
                                                                          title="Нормальное распределение B")),
                          ]
                          ),
            Widgets.Column(children=[
                Widgets.Column(alignment=Alignments.Start,
                               children=[
                                   Widgets.Row(
                                       children=[Widgets.Text("Кол-во интервалов"),
                                                 Widgets.Button("+", on_tap=self.__plus_interval),
                                                 Widgets.Text(str(self._intervals_count)),
                                                 Widgets.Button("-", on_tap=self.__minus_interval)]),
                                   Widgets.Row(
                                       children=[self._name_field,
                                                 Widgets.Button("Загрузить данные", on_tap=self.__load_data)])
                               ]),
                Widgets.Column(alignment=Alignments.Start,
                               children=[
                                   Widgets.Text("Общая информация"),
                                   Widgets.Text(f"Минимум A:\t {self.__data[0].min()}"),
                                   Widgets.Text(f"Среднее A:\t {self.__data[0].mean()}"),
                                   Widgets.Text(f"Максимум A:\t {self.__data[0].max()}"),
                                   Widgets.Container(height=10),
                                   Widgets.Text(f"Минимум B:\t {self.__data[1].min()}"),
                                   Widgets.Text(f"Среднее B:\t {self.__data[1].mean()}"),
                                   Widgets.Text(f"Максимум B:\t {self.__data[1].max()}")
                               ])
            ])
        ])
        self._window.resize(self.WIDTH, self.HEIGHT)
        self._window.setWindowTitle(self.TITLE)
        self._window.show()

    def __plus_interval(self):
        self._intervals_count += 1
        self.__build()

    def __minus_interval(self):
        if self._intervals_count > 1:
            self._intervals_count -= 1
            self.__build()

    def __load_data(self):
        self.__data = numpy.array(Functions.get_data(self._name_field.text()))
        self.__build()

    def __save_data(self):
        ...

    def run(self):
        sys.exit(self._app.exec_())
