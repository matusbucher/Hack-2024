from math import sqrt

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

    def __init__(self, day, month, beginYear, endYear) -> None:
        self.day = day
        self.month = month
        self.beginYear = beginYear
        self.endYear = endYear
        self.data = dict()

    def __repr__(self) -> str:
        return f"{self.day:02}.{self.month:02}."
    
    def loadData(self, data, *measurements) -> None:
        year = self.beginYear
        while year <= self.endYear:
            if year in [int(y) for y in data[f"{self.day:02}.{self.month:02}."].keys()]:
                self.data[year] = {m:data[f"{self.day:02}.{self.month:02}."][str(year)][m] for m in measurements}
            year += 1

    def weightedAverage(self, measurement) -> float:
        weightsDifference = 1
        rateIncrement = weightsDifference / (self.endYear - self.beginYear)
        sum = 0
        num = 0
        currentCoefficient = 1
        for year in range(self.beginYear, self.endYear + 1):
            if year in self.data:
                sum += self.data[year][measurement] * currentCoefficient
                num += 1
            currentCoefficient += rateIncrement
        return sum / (num + rateIncrement * ((num - 1) * (num / 2)))

    def average(self, measurement) -> float:
        sum = 0
        num = 0
        for year in range(self.beginYear, self.endYear + 1):
            if year in self.data:
                sum += self.data[year][measurement]
                num += 1
        return sum / num
    
    def averageFromYears(self, measurement, years):
        sum = 0
        num = 0
        for year in years:
            if year in self.data:
                sum += self.data[year][measurement]
                num += 1
        return sum / num

    def variance(self, measurement) -> float:
        average = self.average(measurement)
        numOfYears = self.endYear - self.beginYear + 1
        sum = 0
        for year in range(self.beginYear, self.endYear + 1):
            if year in self.data:
                sum += pow(self.data[year][measurement] - average, 2)
        return sum / numOfYears
    
    def standardDeviation(self, measurement) -> float:
        return sqrt(self.variance(measurement))
