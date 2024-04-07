from Date import Date
import DataAnalyser
from random import choice

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
    
    def get_lore(self, date: Date):
        s_date = f"{date.day:02}.{date.month:02}."
        dayCounts = [31,28,31,30,31,30,31,31,30,31,30,31]

        maximum = None
        maxima = self.globalMaxima()

        minimum = None
        minima = self.globalMinima()

        for meas in self.measurements:
            if maxima[meas][0] == s_date:
                maximum = maxima[meas][1]
            
            if minima[meas][0] == s_date:
                minimum = minima[meas][1]
        

        if minimum is not None:
            if maximum is not None and abs(minimum) < abs(maximum):
                # call abs maximum
                pass
            else:
                # call abs minimum
                pass
        
        variences = self.day_variences(date)
        if variences != {}:
            meas = choice(variences.keys())
            # call varience with variences[meas]
        
        month_maximum = None
        month_maxima = self.monthMaxima(date.month)
        month_minimum = None
        month_minima = self.monthMinima(date.month)

        for meas in self.measurements:
            if month_maxima[meas][0] == s_date:
                month_maximum = month_maxima[meas][1]
            
            if month_minima[meas][0] == s_date:
                month_minimum = month_minima[meas][1]

        if month_minimum is not None:
            if month_maximum is not None and abs(month_minimum) < abs(month_maximum):
                # call month maximum
                pass
            else:
                # call month minimum
                pass
        
        der_maximum = None
        der_maxima = self.globalMaximumDerivative(date.month)
        der_minimum = None
        der_minima = self.globalMinimumDerivative(date.month)

        for meas in self.measurements:
            if der_maxima[meas][0] == s_date:
                der_maximum = der_maxima[meas][1]
            
            if der_minima[meas][0] == s_date:
                der_minimum = der_minima[meas][1]

        if der_minimum is not None:
            if der_maximum is not None and abs(der_minimum) < abs(der_maximum):
                # call abs der maximum
                pass
            else:
                # call abd der minimum
                pass
        
        month_der_maximum = None
        month_der_maxima = self.monthMaxima(date.month)
        month_der_minimum = None
        month_der_minima = self.monthMinima(date.month)

        for meas in self.measurements:
            if month_der_maxima[meas][0] == s_date:
                month_der_maximum = month_der_maxima[meas][1]
            
            if month_der_minima[meas][0] == s_date:
                month_der_minimum = month_der_minima[meas][1]

        if month_der_minimum is not None:
            if month_der_maximum is not None and abs(month_der_minimum) < abs(month_der_maximum):
                # call month der maximum
                pass
            else:
                # call month der minimum
                pass
        
        for meas1 in self.measurements:
            for meas2 in self.measurements:

                corelation_month = (DataAnalyser.hasCorrelationToDates(date, self.dates[sum(dayCounts[:date.month - 1]):sum(dayCounts[:date.month])], meas1, meas2, 0.6, 0.6))
                
                corelation_year = DataAnalyser.hasCorrelationToDates(date, self.dates,meas1, meas2, 0.6, 0.6)

        corelation_day = DataAnalyser.biggestCorrelationCoefficient(date, self.dates, self.measurements)
        
        


    
