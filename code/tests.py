from Date import *
import unittest

class TestDateMethods(unittest.TestCase):

    def test_loadData(self):
        data = {"01.01.":{2000:{"cloud_cover":10,
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
                              "wind_speed":0,
                              "rain_mm":0,
                              "snow_mm":0}},
                "02.01.":{2000:{"cloud_cover":0,
                              "temperature":0,
                              "wind_speed":0,
                              "rain_mm":0,
                              "snow_mm":0},
                        2002:{"cloud_cover":0,
                              "temperature":0,
                              "wind_speed":0,
                              "rain_mm":0,
                              "snow_mm":0}},
                "03.01.":{2000:{"cloud_cover":0,
                              "temperature":0,
                              "wind_speed":0,
                              "rain_mm":0,
                              "snow_mm":0},
                        2001:{"cloud_cover":0,
                              "temperature":0,
                              "wind_speed":0,
                              "rain_mm":0,
                              "snow_mm":0},
                        2002:{"cloud_cover":0,
                              "temperature":0,
                              "wind_speed":0,
                              "rain_mm":0,
                              "snow_mm":0}}}
        date = Date(1, 1, 2000, 2002)
        date.loadData(data, "cloud_cover", "temperature", "wind_speed", "rain_mm", "snow_mm")

        self.assertEqual(data["01.01."], date.data)

if __name__ == '__main__':
    unittest.main()
