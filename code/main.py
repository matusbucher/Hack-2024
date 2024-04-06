from Date import Date
import DataAnalyser

class Program:
    """
    Field:
    data          All weather data imported from a json file
    dates           dictionary of instances of the Date class for each day of the year (omitting 29th of February lol)   
    """
    def __init__(self, data):
        self.data = data
        self.measurements = ["cloud_cover", "temperature", "wind_speed", "rain_mm", "snow_mm"]
        _day_counts = [31,28,31,30,31,30,31,31,30,31,30,31]
        self.dates = list()
        month = 1
        for num in _day_counts:
            for d in range(num):
                date = Date(d+1, month, 2000, 2023)
                date.loadData(self.dates, *self.measurements)
                self.dates.append(date)
            month += 1

    def globalMaxima(self): #Returns dict of global maxima for all measurements
        return {m:DataAnalyser.globalMaximum(self.dates, m) for m in self.measurements}
    
    def globalMinima(self): #Returns dict of global minima for all measurements
        return {m:DataAnalyser.globalMinimum(self.dates, m) for m in self.measurements}
    
    def globalMaximumDerivative(self): #Returns dict of global maxima of derivatives for all measurements
        return {m:DataAnalyser.globalMaximumDerivative(self.dates, m, 1) for m in self.measurements}
    
    def globalMinimumDerivative(self): #Returns dict of global minima of derivatives for all measurements
        return {m:DataAnalyser.globalMaximumDerivative(self.dates, m, 0) for m in self.measurements}
    
    def globalMaximumCorrelation(self): #Returns dict of global biggest cor. coef. for all days
        return {d:DataAnalyser.biggestCorrelationCoefficient(d, self.dates, self.measurements) for d in self.dates}