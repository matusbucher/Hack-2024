from Date import Date
import DataAnalyser

class Program:
    """
    Field:
    data          All weather data imported from a json file
    dates         dictionary of instances of the Date class for each day of the year (omitting 29th of February lol)   
    """
    def __init__(self, data):
        self.data = data
        self.measurements = ["cloud_cover", "temperature", "wind_speed", "rain_mm", "snow_mm"]
        dayCounts = [31,28,31,30,31,30,31,31,30,31,30,31]
        self.dates = list()
        month = 1
        for num in dayCounts:
            for d in range(num):
                date = Date(d+1, month, 2000, 2023)
                date.loadData(self.data, *self.measurements)
                self.dates.append(date)
            month += 1

    def globalMaxima(self): #Returns dict of global maxima for all measurements
        return {m:DataAnalyser.globalMaximum(self.dates, m) for m in self.measurements}
    
    def monthMaxima(self, month: int): # returns dict of moth maxima for all measurements
        dayCounts = [31,28,31,30,31,30,31,31,30,31,30,31]
        month -= 1
        return {m:DataAnalyser.globalMaximum(self.dates[sum(dayCounts[:month]):sum(dayCounts[:month + 1])], m) for m in self.measurements}
    
    def globalMinima(self): #Returns dict of global minima for all measurements
        return {m:DataAnalyser.globalMinimum(self.dates, m) for m in self.measurements}
    
    def monthMinima(self, month: int): # returns dict of moth minima for all measurements
        dayCounts = [31,28,31,30,31,30,31,31,30,31,30,31]
        month -= 1
        return {m:DataAnalyser.globalMinimum(self.dates[sum(dayCounts[:month]):sum(dayCounts[:month + 1])], m) for m in self.measurements}
    
    def globalMaximumDerivative(self): #Returns dict of global maxima of derivatives for all measurements
        return {m:DataAnalyser.globalMaximumDerivative(self.dates, m, True) for m in self.measurements}
    
    def monthMaximumDerivate(self, month: int): #Returns dict of month maxima of derivatives for all measurements
        dayCounts = [31,28,31,30,31,30,31,31,30,31,30,31]
        month -= 1
        return {m:DataAnalyser.globalMaximumDerivative(self.dates[sum(dayCounts[:month]):sum(dayCounts[:month + 1])], m, True) for m in self.measurements}
    
    def globalMinimumDerivative(self): #Returns dict of global minima of derivatives for all measurements
        return {m:DataAnalyser.globalMaximumDerivative(self.dates, m, False) for m in self.measurements}
    
    def monthMinimumDerivate(self, month: int): #Returns dict of month maxima of derivatives for all measurements
        dayCounts = [31,28,31,30,31,30,31,31,30,31,30,31]
        month -= 1
        return {m:DataAnalyser.globalMaximumDerivative(self.dates[sum(dayCounts[:month]):sum(dayCounts[:month + 1])], m, False) for m in self.measurements}
    
    def globalMaximumCorrelation(self): #Returns dict of global biggest cor. coef. for all days
        return {d:DataAnalyser.biggestCorrelationCoefficient(d, self.dates, self.measurements) for d in self.dates}
    
    def day_variences(self, date: Date): #Returns dict of measurments[tuple[bool, avg for day]], true - stable, false - unstable
        magic_coefs = {"cloud_cover": 0.1, "temperature": 3, "wind_speed": 3, "rain_mm": 0.2, "snow_mm": 0.2}
        d = {}
        for measurement in self.measurements:
            variation = date.standardDeviation(measurement)
            if variation < magic_coefs[measurement]:
                d[measurement] = (True, date.average(measurement))
            elif variation < magic_coefs[measurement]*3:
                d[measurement] = (False, 0)

        return d
    
