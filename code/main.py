from Date import Date

class Program:
    """
    Field:
    data          All weather data imported from a json file
    day           dictionary of instances of the Date class for each day of the year (omitting 29th of February lol)   
    """
    def __init__(self, data):
        self.data = data
        self._day_counts = [31,28,31,30,31,30,31,31,30,31,30,31]
        self.day = {}
        self._month = 1
        for num in self._day_counts:
            for d in range(num):
                self.day[f"{d+1}.{self._month:02}."] = Date(d+1, self._month, 2000, 2023)
                self.day[f"{d+1}.{self._month:02}."].loadData(self.data, "cloud_cover", "temperature", "wind_speed", "rain_mm", "snow_mm")
            self._month += 1