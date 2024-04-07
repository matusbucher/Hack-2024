from Date import Date
import data_analyser
import prompter
from json import loads
from random import choice

class Program:
    """
    Field:
    data          All weather data imported from a json file
    dates         dictionary of instances of the Date class for each day of the year (omitting 29th of February lol)   
    """

    MEASUREMENTS = {"cloud_cover":"cloud coverage",
                    "temperature":"temperature",
                    "wind_speed":"wind speed",
                    "rain_mm":"amount of rain",
                    "snow_mm":"amount of snow"}

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
        return {m:data_analyser.globalMaximum(self.dates, m) for m in self.measurements}
    
    def monthMaxima(self, month: int): # returns dict of moth maxima for all measurements
        dayCounts = [31,28,31,30,31,30,31,31,30,31,30,31]
        month -= 1
        return {m:data_analyser.globalMaximum(self.dates[sum(dayCounts[:month]):sum(dayCounts[:month + 1])], m) for m in self.measurements}
    
    def globalMinima(self): #Returns dict of global minima for all measurements
        return {m:data_analyser.globalMinimum(self.dates, m) for m in self.measurements}
    
    def monthMinima(self, month: int): # returns dict of moth minima for all measurements
        dayCounts = [31,28,31,30,31,30,31,31,30,31,30,31]
        month -= 1
        return {m:data_analyser.globalMinimum(self.dates[sum(dayCounts[:month]):sum(dayCounts[:month + 1])], m) for m in self.measurements}
    
    def globalMaximumDerivative(self): #Returns dict of global maxima of derivatives for all measurements
        return {m:data_analyser.globalMaximumDerivative(self.dates, m, True) for m in self.measurements}
    
    def monthMaximumDerivate(self, month: int): #Returns dict of month maxima of derivatives for all measurements
        dayCounts = [31,28,31,30,31,30,31,31,30,31,30,31]
        month -= 1
        return {m:data_analyser.globalMaximumDerivative(self.dates[sum(dayCounts[:month]):sum(dayCounts[:month + 1])], m, True) for m in self.measurements}
    
    def globalMinimumDerivative(self): #Returns dict of global minima of derivatives for all measurements
        return {m:data_analyser.globalMaximumDerivative(self.dates, m, False) for m in self.measurements}
    
    def monthMinimumDerivate(self, month: int): #Returns dict of month maxima of derivatives for all measurements
        dayCounts = [31,28,31,30,31,30,31,31,30,31,30,31]
        month -= 1
        return {m:data_analyser.globalMaximumDerivative(self.dates[sum(dayCounts[:month]):sum(dayCounts[:month + 1])], m, False) for m in self.measurements}
    
    def globalMaximumCorrelation(self): #Returns dict of global biggest cor. coef. for all days
        return {d:data_analyser.biggestCorrelationCoefficient(d, self.dates, *self.measurements) for d in self.dates}
    
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
    
    def get_lore(self, date: Date) -> tuple[str, str]:
        dayCounts = [31,28,31,30,31,30,31,31,30,31,30,31]
        ai = prompter.LoreGenerator(date.get_str())

        maxima = self.globalMaxima()
        minima = self.globalMinima()

        for meas in self.measurements:
            if maxima[meas][0].get_str() == date.get_str():
                return (ai.prompt_extreme(meas, True, True), f"{date} was yearly maximum in measurement: {self.MEASUREMENTS[meas]} in {round(maxima[meas][2]*100, 2)}% of years.")
            
            if minima[meas][0].get_str() == date.get_str():
                return (ai.prompt_extreme(meas, True, False), f"{date} was yearly minimum in measurement: {self.MEASUREMENTS[meas]} in {round(minima[meas][2]*100, 2)}% of years.")
        
        
        #variences = self.day_variences(date)
        #if variences != {}:
        #    meas = choice(list(variences.keys()))
        #    return ai.prompt_variability(meas, variences[meas][0], variences[meas][1])
        
        month_maxima = self.monthMaxima(date.month)
        month_minima = self.monthMinima(date.month)

        for meas in self.measurements:
            if month_maxima[meas][0].get_str() == date.get_str():
                return (ai.prompt_extreme(meas, False, True), f"{date} was monthly maximum in measurement: {self.MEASUREMENTS[meas]} in {round(month_maxima[meas][2]*100, 2)}% of years.")
            
            if month_minima[meas][0].get_str() == date.get_str():
                return (ai.prompt_extreme(meas, False, False), f"{date} was monthly minimum in measurement: {self.MEASUREMENTS[meas]} in {round(month_minima[meas][2]*100, 2)}% of years.")
        
        der_maxima = self.globalMaximumDerivative()
        der_minima = self.globalMinimumDerivative()

        for meas in self.measurements:
            if der_maxima[meas][0].get_str() == date.get_str():
                return (ai.prompt_growth_extreme(meas, True, True), f"{date} has the highest increase in measurement: {self.MEASUREMENTS[meas]} over whole year in {round(der_maxima[meas][2]*100, 2)}% of years.")
            
            if der_minima[meas][0].get_str() == date.get_str():
                return (ai.prompt_growth_extreme(meas, False, True), f"{date} has the highest decrease in measurement: {self.MEASUREMENTS[meas]} over whole year in {round(der_minima[meas][2]*100, 2)}% of years.")
        
        month_der_maxima = self.monthMaximumDerivate(date.month)
        month_der_minima = self.monthMinimumDerivate(date.month)

        for meas in self.measurements:
            if month_der_maxima[meas][0].get_str() == date.get_str():
                return (ai.prompt_growth_extreme(meas, True, False), f"{date} has the highest increase in measurement: {self.MEASUREMENTS[meas]} over the month in {round(month_der_maxima[meas][2]*100, 2)}% of years.")
            
            if month_der_minima[meas][0].get_str() == date.get_str():
                return (ai.prompt_growth_extreme(meas, False, False), f"{date} has the highest decrease in measurement: {self.MEASUREMENTS[meas]} over the month in {round(month_der_minima[meas][2]*100, 2)}% of years.")
        
        for meas1 in self.measurements:
            for meas2 in self.measurements:
                #corelation_year = data_analyser.hasCorrelationToDates(date, self.dates,meas1, meas2, 0.6, 0.6)
                #if corelation_year[0]:
                #    return ai.prompt_correlation_pair(meas1, meas2, date.month, corelation_month[1] > 0, 2)

                corelation_month = (data_analyser.hasCorrelationToDates(date, self.dates[sum(dayCounts[:date.month - 1]):sum(dayCounts[:date.month])], meas1, meas2, 0.6, 0.6))
                if corelation_month[0]:
                    return (ai.prompt_correlation_pair(meas1, meas2, date.month, corelation_month[1] > 0, 1), f"{round(corelation_month[2]*100, 2)}% of days in the month after {date} had strong {'positive' if corelation_month[1] > 0 else 'negative'} correlation with the measurement of: {self.MEASUREMENTS[meas]}.")
                
        corelation_day = data_analyser.biggestCorrelationCoefficient(date, self.dates, *self.measurements)

        last_d = corelation_day[0]
        last_last_date = f"{last_d.day:02}.{last_d.month:02}."

        return (ai.prompt_correlation_pair(corelation_day[1], corelation_day[2], last_last_date, corelation_day[3] > 0, 0), f"Measurement: {self.MEASUREMENTS[corelation_day[1]]} at {date} and measurement: {self.MEASUREMENTS[corelation_day[2]]} at {last_last_date} had strong {'positive' if corelation_day[3] > 0 else 'negative'} correlation in {round(corelation_day[4]*100, 2)}% of years.")

if __name__ == "__main__":
    j = open("../data/model_data1.json", "r")
    json_data = loads(j.read())
    data = {}
    tmp = {}
    for date, year in json_data.items():
        for y, r in year.items():
            tmp[int(y)] = r
        data[date] = tmp.copy()

    p = Program(data)
    prompt = p.get_lore(Date(21, 9, 2000, 2024).loadData(data, *p.measurements))

    print(prompt)
