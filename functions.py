import matplotlib.pyplot
import numpy
import pandas

import settings


class Functions:
    @staticmethod
    def get_scatter(list_x: numpy.array, list_y: numpy.array, title: str = ""):
        matplotlib.pyplot.close()
        fig, ax = matplotlib.pyplot.subplots(1)
        ax.scatter(list_x, list_y)
        ax.set_title(title)
        return fig

    @staticmethod
    def get_two_plots(list_x: numpy.array, list_y: numpy.array, title: str = ""):
        matplotlib.pyplot.close()
        fig, ax = matplotlib.pyplot.subplots(1)
        ax.plot(list_x)
        ax.plot(list_y)
        ax.set_title(title)
        return fig

    @staticmethod
    def get_intervals(data_list: numpy.array, intervals_count: int, title: str = ""):
        fig, ax = matplotlib.pyplot.subplots(1)

        first_condition = lambda i: data_list >= min(data_list) + i * (
                max(data_list) - min(data_list)) / intervals_count
        second_condition = lambda i: data_list < min(data_list) + (i + 1) * (
                max(data_list) - min(data_list)) / intervals_count

        intervals = [data_list[(first_condition(i)) & (second_condition(i))].size for i in range(intervals_count)]
        ax.bar(numpy.linspace(min(data_list), max(data_list) + 1e-10, num=intervals_count),
               intervals, width=(max(data_list) - min(data_list)) / intervals_count * 0.9, align="edge")
        ax.set_title(title)
        return fig

    @staticmethod
    def sort_np_data(data: numpy.ndarray) -> numpy.ndarray:
        return numpy.array(sorted(list([tuple(i) for i in data])))

    @staticmethod
    def get_data(file_name):
        return pandas.read_excel(settings.INPUT_FILE_DIRECTORY + file_name).to_numpy()

    @staticmethod
    def normalize(data_list: numpy.array):
        return (data_list - data_list.min()) / (data_list.max() - data_list.min())
