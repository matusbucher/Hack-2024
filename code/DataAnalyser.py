from Date import *

def globalMaximum(dates, measurement):
    if len(dates) == 0:
        return None
    return max([d.weightedAverage(measurement) for d in dates])


def globalMinimum(dates, measurement):
    if len(dates) == 0:
        return None
    return min([d.weightedAverage(measurement) for d in dates])
