from Date import *
from math import sqrt

def globalMaximum(dates, measurement) -> tuple[Date, float]:
    if len(dates) == 0:
        return None
    
    date = dates[0]
    maximum = dates[0].weightedAverage(measurement)

    for d in dates[1:]:
        if d.weightedAverage(measurement) > maximum:
            date = d
            maximum = d.weightedAverage(measurement)

    return (date, maximum)


def globalMinimum(dates, measurement) -> tuple[Date, float]:
    if len(dates) == 0:
        return None
    
    date = dates[0]
    minimum = dates[0].weightedAverage(measurement)

    for d in dates[1:]:
        if d.weightedAverage(measurement) < minimum:
            date = d
            minimum = d.weightedAverage(measurement)

    return (date, minimum)


def globalMaximumDerivative(dates, measurement, positive) -> tuple[Date, float]:
    if len(dates) <= 1 or not isinstance(positive, bool):
        return None
    
    date = dates[0]
    maximum = dates[0 + int(positive)].weightedAverage(measurement) - dates[1 - int(positive)].weightedAverage(measurement)

    for i in range(1, len(dates) - 1):
        if dates[i].weightedAverage(measurement) - dates[i+1].weightedAverage(measurement) > maximum:
            date = date
            maximum = dates[i+1].weightedAverage(measurement) - dates[i].weightedAverage(measurement)

    return (date, maximum)

def correlationCoefficient(date_1, date_2, measurement_1, measurement_2) -> float:
    date_1_avg = date_1.weightedAverage(measurement_1)
    date_2_avg = date_2.weightedAverage(measurement_2)
    start_year = 2000
    end_year = 2023
    # Nepytaj sa
    return sum([(date_1.data[start_year + i][measurement_1] - date_1_avg) * (date_2.data[start_year + i][measurement_2] - date_2_avg) for i in range(end_year - start_year + 1)]) / ((sqrt(sum([(date_1.data[start_year + i][measurement_1] - date_1_avg)**2 for i in range(end_year - start_year + 1)]))) * (sqrt(sum([(date_2.data[start_year + i][measurement_2] - date_2_avg)**2 for i in range(end_year - start_year + 1)]))))

def biggestCorrelationCoefficient(date, dates, *measurements) -> tuple[str, float]:
    biggest = ("None", 0)
    for m in measurements:
        for mm in measurements:
            for day in dates:
                if day != date:
                    c = correlationCoefficient(date, day, m, mm)
                    if c > biggest[1]:
                        biggest = (f"{day} {m} {mm}", c)
    return biggest





