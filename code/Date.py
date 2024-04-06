class Date:

    URL_DATA_SERVER = "https://ogimet.com/display_synops2.php?lang=en"
    DEFAULT_WMO_INDEX = 11968

    def __init__(self, day, month, beginYear, endYear) -> None:
        self.day = day
        self.month = month
        self.beginYear = beginYear
        self.endYear = endYear
        self.wmoIndex = self.DEFAULT_WMO_INDEX
        self.data = dict()

    def setWmoIndex(self, index):
        self.wmoIndex = index
    
    def loadData(self, measurements):
        pass

    def weightedAverageGraph(self):
        pass

    #TODO dalsie metody