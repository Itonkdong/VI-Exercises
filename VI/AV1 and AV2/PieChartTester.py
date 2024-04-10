class PieChart:

    def __init__(self, values):
        self.starting_values = values
        self.chart = self.__compute_chart()

    def __compute_chart(self):
        computed_chart = {}
        total = sum(self.starting_values.values())
        for (key, value) in self.starting_values.items():
            freq = value / total * 360
            computed_chart[key] = round(freq, 1)

        return computed_chart

    def __str__(self):
        return str(self.chart)


chart1 = PieChart({"a": 1, "b": 2})
print(chart1)
chart2 = PieChart({"a": 30, "b": 15, "c": 55})
print(chart2)
chart3 = PieChart({"a": 8, "b": 21, "c": 12, "d": 5, "e": 4})
print(chart3)
