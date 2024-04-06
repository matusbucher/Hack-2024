from Date import Date
import DataAnalyser

class Program:
    """
    Field:
    data          All weather data imported from a json file
    day           dictionary of instances of the Date class for each day of the year (omitting 29th of February lol)   
    """
    def __init__(self, data):
        self.data = data
        self.measurements = ["cloud_cover", "temperature", "wind_speed", "rain_mm", "snow_mm"]
        _day_counts = [31,28,31,30,31,30,31,31,30,31,30,31]
        self.day = {}
        _month = 1
        for num in _day_counts:
            for d in range(num):
                self.day[f"{d+1}.{_month:02}."] = Date(d+1, self._month, 2000, 2023)
                self.day[f"{d+1}.{_month:02}."].loadData(self.data, self.measurements)
            _month += 1

    def globalMaxima(self): #Returns dict of global maxima for all measurements
        return {m:DataAnalyser.globalMaximum(self.day.values(), m) for m in self.measurements}
    
    def globalMinima(self): #Returns dict of global minima for all measurements
        return {m:DataAnalyser.globalMaximum(self.day.values(), m) for m in self.measurements}