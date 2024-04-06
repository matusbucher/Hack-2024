from Date import *

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
