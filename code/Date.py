import requests

class Date:

    """
    Field:
    day         day of the date (as integer)
    month       month of the date (as integer)
    beginYear   first year of the processed data
    endYear     last year of the processed data
    wmoIndex    WMO synop index of the station
    data        dictionary with data of all measurements for every year from range [beginYear - endYear] (both including)
    """

    URL_DATA_SERVER = "https://ogimet.com/display_synops2.php?lang=en"
    DEFAULT_WMO_INDEX = 11968

    def __init__(self, day, month, beginYear, endYear) -> None:
        self.day = day
        self.month = month
        self.beginYear = beginYear
        self.endYear = endYear
        self.wmoIndex = self.DEFAULT_WMO_INDEX
        self.data = dict()

    def setWmoIndex(self, index) -> None:
        self.wmoIndex = index
    
    def loadData(self, data, *measurements):
        self.year = self.beginYear
        while self.year > self.endYear:
            self.data[self.year] = {m:data[f"{self.day:02}.{self.month:02}."][self.year][m] for m in measurements}
            self.year += 1

    def weightedAverage(self, measurement) -> float:
        numOfYears = self.endYear - self.beginYear + 1
        weightsDifference = 1
        rateIncrement = weightsDifference / (numOfYears - 1)
        divisionCoefficient = numOfYears + rateIncrement * ((numOfYears - 1) * (numOfYears / 2))

        sum = 0
        currentCoefficient = 1
        for year in range(self.beginYear, self.endYear + 1):
            if year in self.data:
                sum += self.data[year][measurement] * currentCoefficient
                currentCoefficient += rateIncrement

        return (sum / divisionCoefficient)

    def average(self, measuremnet) -> float:
        numOfYears = self.endYear - self.beginYear + 1
        sum = 0
        for year in range(self.beginYear, self.endYear + 1):
            if year in self.data:
                sum += self.data[year][measuremnet]

        return sum / numOfYears

    def variance(self, measurement) -> float:
        average = self.average(measurement)
        numOfYears = self.endYear - self.beginYear + 1
        sum = 0
        for year in range(self.beginYear, self.endYear + 1):
            if year in self.data:
                sum += pow(self.data[year][measurement] - average, 2)
        return sum / numOfYears

    # TODO dalsie metody

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


