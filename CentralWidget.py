from PyQt6.QtCharts import QChartView, QChart, QDateTimeAxis, QValueAxis, QSplineSeries
from PyQt6.QtCore import Qt, QDateTime, pyqtSlot


class CentralWidget(QChartView):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.__value_start = QSplineSeries()
        self.__value_high = QSplineSeries()
        self.__value_low = QSplineSeries()
        self.__value_end = QSplineSeries()

        # Requirement 2.6

    @pyqtSlot(str)
    def append_values(self, line):
        cells = line.split(";")

        datetime = QDateTime.fromString(cells[0], "dd.MM.yyyy").toMSecsSinceEpoch()

        start = self.currency_to_float(cells[1])
        self.__value_start.append(datetime, start)

        high = self.currency_to_float(cells[2])
        self.__value_high.append(datetime, high)

        low = self.currency_to_float(cells[3])
        self.__value_low.append(datetime, low)

        end = self.currency_to_float(cells[4])
        self.__value_end.append(datetime, end)

    def currency_to_float(self, string):
        tokens = string.split(" ")

        float_value = tokens[0].replace(",", ".")

        tmp = float(float_value)

        return tmp
