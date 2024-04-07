from Date import *
from math import sqrt
from typing import *

def globalMaximum(dates: Collection[Date], measurement: str) -> tuple[Date, float, float]:
    if len(dates) == 0:
        return None
    
    date = dates[0]
    maximumAvg = dates[0].weightedAverage(measurement)
    for d in dates[1:]:
        if d.weightedAverage(measurement) > maximumAvg:
            date = d
            maximumAvg = d.weightedAverage(measurement)
    return (date, maximumAvg, percentageGlobalMaximum(date, dates, measurement))


def globalMinimum(dates: Collection[Date], measurement: str) -> tuple[Date, float, float]:
    if len(dates) == 0:
        return None
    
    date = dates[0]
    minimumAvg = dates[0].weightedAverage(measurement)

    for d in dates[1:]:
        if d.weightedAverage(measurement) < minimumAvg:
            date = d
            minimumAvg = d.weightedAverage(measurement)

    return (date, minimumAvg, percentageGlobalMinimum(date, dates, measurement))


def globalMaximumDerivative(dates: Collection[Date], measurement: str, positive: bool) -> tuple[Date, float]:
    if len(dates) <= 1 or not isinstance(positive, bool):
        return None
    
    date = dates[0]
    followingDate = dates[1]
    maximumAvgDiff = dates[0 + int(positive)].average(measurement) - dates[1 - int(positive)].average(measurement)
    for i in range(1, len(dates) - 1):
        if dates[i + int(positive)].average(measurement) - dates[i+1 - int(positive)].average(measurement) > maximumAvgDiff:
            date = dates[i]
            followingDate = dates[i+1]
            maximumAvgDiff = dates[i + int(positive)].average(measurement) - dates[i+1 - int(positive)].average(measurement)
    return (date, maximumAvgDiff, percentageGlobalMaximumDerivative(date, followingDate, measurement, positive, maximumAvgDiff + (-1)**(int(positive)) * (abs(maximumAvgDiff) * 0.1)))

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

def hasCorrelationToDates(date: Date, dates: Collection[Date], measurement_1: str, measurement_2: str, minAbsCorrelCoef: float, minPercentage: float) -> tuple[bool, float]:
    if minAbsCorrelCoef < -1 or minAbsCorrelCoef > 1 or minPercentage > 1 or minPercentage <= 0.5:
        return (False, 0)
    
    numPositiveCorrelation = 0
    numNegativeCorrelation = 0
    sumCorrelCoef = 0
    for d in dates:
        r = correlationCoefficient(date, d, measurement_1, measurement_2)
        sumCorrelCoef += r
        if abs(r) >= minAbsCorrelCoef:
            if r > 0:
                numPositiveCorrelation += 1
            elif r < 0:
                numNegativeCorrelation += 1
    avgCorrelCoef = sumCorrelCoef / len(dates)
    
    if abs(avgCorrelCoef) >= minAbsCorrelCoef and (numPositiveCorrelation / len(dates) >= minPercentage or numNegativeCorrelation / len(dates) >= minPercentage):
        return (True, avgCorrelCoef)
    return (False, 0)


def percentageGlobalMaximum(date: Date, dates: Collection[Date], measurement: str) -> float:
    num = 0
    for year in date.data:
        if date.data[year][measurement] == max([d.data[year][measurement] for d in dates if year in d.data]):
            num += 1
    return num / len(date.data)


def percentageGlobalMinimum(date: Date, dates: Collection[Date], measurement: str) -> float:
    num = 0
    for year in date.data:
        if date.data[year][measurement] == min([d.data[year][measurement] for d in dates if year in d.data]):
            num += 1
    return num / len(date.data)


def percentageGlobalMaximumDerivative(date: Date, followingDate: Date, measurement: str, positive: bool, minDiff: float) -> float:
    num = 0
    years = set(date.data.keys()).intersection(followingDate.data.keys())
    for year in years:
        diff = followingDate.data[year][measurement] - date.data[year][measurement] if positive else date.data[year][measurement] - followingDate.data[year][measurement]
        if diff >= minDiff:
                num += 1
    return num / len(years)
