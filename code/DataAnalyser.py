from Date import *
from math import sqrt
from typing import *

def globalMaximum(dates: Collection[Date], measurement: str) -> tuple[Date, float]:
    if len(dates) == 0:
        return None
    
    date = dates[0]
    maximum = dates[0].weightedAverage(measurement)
    for d in dates[1:]:
        if d.weightedAverage(measurement) > maximum:
            date = d
            maximum = d.weightedAverage(measurement)
    return (date, maximum)


def globalMinimum(dates: Collection[Date], measurement: str) -> tuple[Date, float]:
    if len(dates) == 0:
        return None
    
    date = dates[0]
    minimum = dates[0].weightedAverage(measurement)

    for d in dates[1:]:
        if d.weightedAverage(measurement) < minimum:
            date = d
            minimum = d.weightedAverage(measurement)

    return (date, minimum)


def globalMaximumDerivative(dates: Collection[Date], measurement: str, positive: bool) -> tuple[Date, float]:
    if len(dates) <= 1 or not isinstance(positive, bool):
        return None
    
    date = dates[0]
    maximum = dates[0 + int(positive)].weightedAverage(measurement) - dates[1 - int(positive)].weightedAverage(measurement)
    for i in range(1, len(dates) - 1):
        if dates[i + int(positive)].weightedAverage(measurement) - dates[i+1 - int(positive)].weightedAverage(measurement) > maximum:
            date = dates[i]
            maximum = dates[i + int(positive)].weightedAverage(measurement) - dates[i+1 - int(positive)].weightedAverage(measurement)
    return (date, maximum)

def correlationCoefficient(date_1: Date, date_2: Date, measurement_1: str, measurement_2: str) -> float:
    years = set(date_1.data.keys()).intersection(date_2.data.keys())

    if (len(years) == 0):
        return None
    
    date_1_avg = date_1.averageFromYears(measurement_1, years)
    date_2_avg = date_2.averageFromYears(measurement_2, years)
    date_1_diffs = [(date_1.data[year][measurement_1] - date_1_avg) for year in years]
    date_2_diffs = [(date_2.data[year][measurement_2] - date_2_avg) for year in years]
    numerator = sum([date_1_diffs[i] * date_2_diffs[i] for i in range(len(years))])
    denominator = sqrt(sum(diff**2 for diff in date_1_diffs) * sum(diff**2 for diff in date_2_diffs))
    
    if denominator == 0:
        return 0
    return numerator / denominator

def biggestCorrelationCoefficient(date: Date, dates: Collection[Date], *measurements: str) -> tuple[Date, str, str, float]:
    biggest = (None, "-", "-", 0)
    for d in dates:
        if d != date:
            for m1 in measurements:
                for m2 in measurements:
                    r = correlationCoefficient(date, d, m1, m2)
                    if abs(r) > abs(biggest[3]):
                        biggest = (d, m1, m2, r)
    return biggest
