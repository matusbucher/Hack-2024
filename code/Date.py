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

    def setData(self, data):
        self.data = data

    # TODO dalsie metody