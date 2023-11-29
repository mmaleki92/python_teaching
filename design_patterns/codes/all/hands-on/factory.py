class Chart:
    def draw(self):
        pass

class BarChart(Chart):
    def draw(self):
        return "Drawing Bar Chart"

class PieChart(Chart):
    def draw(self):
        return "Drawing Pie Chart"

class LineChart(Chart):
    def draw(self):
        return "Drawing Line Chart"

class ChartFactory:
    @staticmethod
    def create_chart(type):
        if type == "bar":
            return BarChart()
        elif type == "pie":
            return PieChart()
        elif type == "line":
            return LineChart()
        else:
            raise ValueError("Unknown Chart Type")

# Usage
chart = ChartFactory.create_chart("pie")
print(chart.draw())  # Drawing Pie Chart
