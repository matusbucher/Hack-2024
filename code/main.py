from Date import Date
import DataAnalyser
import prompter
from json import loads

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
        return {d:DataAnalyser.biggestCorrelationCoefficient(d, self.dates, *self.measurements) for d in self.dates}
    
    def day_variences(self, date: Date): #Returns dict of measurments[tuple[bool, avg for day]], true - stable, false - unstable
        magic_coefs = {"cloud_cover": 0.01, "temperature": 1, "wind_speed": 1, "rain_mm": 0.05, "snow_mm": 0.05}
        d = {}
        for measurement in self.measurements:
            variation = date.standardDeviation(measurement)
            if variation < magic_coefs[measurement]:
                d[measurement] = (True, date.average(measurement))
            elif variation < magic_coefs[measurement]*3:
                d[measurement] = (False, 0)

        return d
    
    def get_lore(self, date: Date):
        dayCounts = [31,28,31,30,31,30,31,31,30,31,30,31]
        ai = prompter.LoreGenerator(date)

        maxima = self.globalMaxima()
        minima = self.globalMinima()

        for meas in self.measurements:
            if maxima[meas][0].get_str() == date.get_str():
                return ai.prompt_extreme(meas, True, True)
            
            if minima[meas][0].get_str() == date.get_str():
                return ai.prompt_extreme(meas, True, False)
        
        
        # variences = self.day_variences(date)
        #if variences != {}:
        #    meas = choice(list(variences.keys()))
        #    return ai.prompt_variability(meas, variences[meas][0], variences[meas][1])
        
        month_maxima = self.monthMaxima(date.month)
        month_minima = self.monthMinima(date.month)

        for meas in self.measurements:
            if month_maxima[meas][0].get_str() == date.get_str():
                return ai.prompt_extreme(meas, False, True)
            
            if month_minima[meas][0].get_str() == date.get_str():
                return ai.prompt_extreme(meas, False, False)
        
        der_maxima = self.globalMaximumDerivative()
        der_minima = self.globalMinimumDerivative()

        for meas in self.measurements:
            if der_maxima[meas][0].get_str() == date.get_str():
                return ai.prompt_growth_extreme(meas, True, True)
            
            if der_minima[meas][0].get_str() == date.get_str():
                return ai.prompt_growth_extreme(meas, False, True)
        
        month_der_maxima = self.monthMaximumDerivate(date.month)
        month_der_minima = self.monthMinimumDerivate(date.month)

        for meas in self.measurements:
            if month_der_maxima[meas][0].get_str() == date.get_str():
                return ai.prompt_growth_extreme(meas, True, False)
            
            if month_der_minima[meas][0].get_str() == date.get_str():
                return ai.prompt_growth_extreme(meas, False, False)
        
        for meas1 in self.measurements:
            for meas2 in self.measurements:
                #corelation_year = DataAnalyser.hasCorrelationToDates(date, self.dates,meas1, meas2, 0.6, 0.6)
                #if corelation_year[0]:
                #    return ai.prompt_correlation_pair(meas1, meas2, date.month, corelation_month[1] > 0, 2)

                corelation_month = (DataAnalyser.hasCorrelationToDates(date, self.dates[sum(dayCounts[:date.month - 1]):sum(dayCounts[:date.month])], meas1, meas2, 0.6, 0.6))
                if corelation_month[0]:
                    return ai.prompt_correlation_pair(meas1, meas2, date.month, corelation_month[1] > 0, 1)
                
        corelation_day = DataAnalyser.biggestCorrelationCoefficient(date, self.dates, *self.measurements)

        last_d = corelation_day[0]
        last_last_date = f"{last_d.day:02}.{last_d.month:02}."


        return ai.prompt_correlation_pair(corelation_day[1], corelation_day[2], last_last_date, corelation_day[3] > 0, 0)
        return "last cor"

if __name__ == "__main__":
    j = open("data/model_data1.json", "r")
    json_data = loads(j.read())
    data = {}
    tmp = {}
    for date, year in json_data.items():
        for y, r in year.items():
            tmp[int(y)] = r
        data[date] = tmp.copy()

    p = Program(data)
    prompt = p.get_lore(Date(13, 7, 2000, 2024).loadData(data, *p.measurements))

    print(prompt)
