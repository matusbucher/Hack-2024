from Date import Date
import data_analyser
import unittest

class TestDateMethods(unittest.TestCase):

    data = {"01.01.":{2000:{"cloud_cover":34,
                              "temperature":5,
                              "wind_speed":32,
                              "rain_mm":69,
                              "snow_mm":0},
                        2001:{"cloud_cover":8,
                              "temperature":-3.5,
                              "wind_speed":15,
                              "rain_mm":0,
                              "snow_mm":20},
                        2002:{"cloud_cover":21,
                              "temperature":9.8,
                              "wind_speed":3,
                              "rain_mm":0,
                              "snow_mm":0}},
                "02.01.":{2000:{"cloud_cover":98,
                              "temperature":0.01,
                              "wind_speed":33,
                              "rain_mm":0,
                              "snow_mm":0},
                        2002:{"cloud_cover":75,
                              "temperature":-5,
                              "wind_speed":13,
                              "rain_mm":0,
                              "snow_mm":125}},
                "03.01.":{2000:{"cloud_cover":66,
                              "temperature":3.2,
                              "wind_speed":64,
                              "rain_mm":17,
                              "snow_mm":0},
                        2001:{"cloud_cover":9,
                              "temperature":0,
                              "wind_speed":25,
                              "rain_mm":0,
                              "snow_mm":0},
                        2002:{"cloud_cover":42,
                              "temperature":1.4,
                              "wind_speed":61,
                              "rain_mm":420,
                              "snow_mm":0}}}
    
    measurements = ("cloud_cover", "temperature", "wind_speed", "rain_mm", "snow_mm")

    def test_loadData(self):
        date0101 = Date(1, 1, 2000, 2002)
        date0101.loadData(self.data, *self.measurements)
        date0201 = Date(2, 1, 2000, 2002)
        date0201.loadData(self.data, *self.measurements)
        date0301 = Date(3, 1, 2000, 2002)
        date0301.loadData(self.data, *self.measurements)
        self.assertEqual(self.data["01.01."], date0101.data)
        self.assertEqual(self.data["02.01."], date0201.data)
        self.assertEqual(self.data["03.01."], date0301.data)
    
    def test_average(self):
        date = Date(1, 1, 2000, 2002)
        date.loadData(self.data, *self.measurements)
        self.assertEqual(round(date.average("temperature"), 2), 3.77)
        self.assertEqual(round(date.weightedAverage("temperature"), 2), 4.3)
    
    def test_standardDeviation(self):
        date = Date(1, 1, 2000, 2002)
        date.loadData(self.data, *self.measurements)
        self.assertEqual(round(date.variance("temperature"), 2), 30.24)
        self.assertEqual(round(date.standardDeviation("temperature"), 2), 5.5)

# end TestDateMethods


class TestDataAnalyserFunctions(unittest.TestCase):

    data = {"01.01.":{2000:{"cloud_cover":34,
                              "temperature":5,
                              "wind_speed":32,
                              "rain_mm":69,
                              "snow_mm":0},
                        2001:{"cloud_cover":8,
                              "temperature":-3.5,
                              "wind_speed":15,
                              "rain_mm":0,
                              "snow_mm":20},
                        2002:{"cloud_cover":21,
                              "temperature":9.8,
                              "wind_speed":3,
                              "rain_mm":0,
                              "snow_mm":0}},
                "02.01.":{2000:{"cloud_cover":98,
                              "temperature":0.01,
                              "wind_speed":33,
                              "rain_mm":0,
                              "snow_mm":0},
                        2002:{"cloud_cover":75,
                              "temperature":-5,
                              "wind_speed":13,
                              "rain_mm":0,
                              "snow_mm":125}},
                "03.01.":{2000:{"cloud_cover":66,
                              "temperature":3.2,
                              "wind_speed":64,
                              "rain_mm":17,
                              "snow_mm":0},
                        2001:{"cloud_cover":9,
                              "temperature":0,
                              "wind_speed":25,
                              "rain_mm":0,
                              "snow_mm":0},
                        2002:{"cloud_cover":42,
                              "temperature":1.4,
                              "wind_speed":61,
                              "rain_mm":420,
                              "snow_mm":0}}}
    
    measurements = ("cloud_cover", "temperature", "wind_speed", "rain_mm", "snow_mm")

    dates = [Date(1, 1, 2000, 2002), Date(2, 1, 2000, 2002), Date(3, 1, 2000, 2002)]
    for date in dates:
        date.loadData(data, *measurements)

    def test_globalMaximumAndMinimum(self):
        ret1 = data_analyser.globalMaximum(self.dates, "temperature")
        self.assertEqual(ret1[0], self.dates[0])
        self.assertEqual(round(ret1[1], 2), 4.3)

        ret2 = data_analyser.globalMinimum(self.dates, "temperature")
        self.assertEqual(ret2[0], self.dates[1])
        self.assertEqual(round(ret2[1], 2), -4)

    def test_globalMaximumDerivative(self):
        ret1 = data_analyser.globalMaximumDerivative(self.dates, "wind_speed", True)
        self.assertEqual(ret1[0], self.dates[1])
        self.assertEqual(round(ret1[1], 2), 27)

        ret2 = data_analyser.globalMaximumDerivative(self.dates, "cloud_cover", False)
        self.assertEqual(ret2[0], self.dates[1])
        self.assertEqual(round(ret2[1], 2), 47.5)

    def test_correlationCoefficient(self):
        ret1 = data_analyser.correlationCoefficient(self.dates[0], self.dates[2], "temperature", "temperature")
        self.assertEqual(round(ret1[0], 2), 0.57)

        ret2 = data_analyser.biggestCorrelationCoefficient(self.dates[0], self.dates, *self.measurements)
        self.assertEqual(ret2[:4], (self.dates[1], "cloud_cover", "cloud_cover", 1.0))

# end TestDataAnalyserFunctions


if __name__ == "__main__":
    unittest.main()
