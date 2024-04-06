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


def globalMaximumDerivation(dates, measurement) -> tuple[Date, float]:
    pass

def globalMinimumDerivation(dates, measurement) -> tuple[Date, float]:
    pass