from main import Program
from Date import Date
from json import loads

j = open("data/model_data1.json", "r")
json_data = loads(j.read())

print(type(json_data))

new = {}
new_dict = {}
for date, year in json_data.items():
    for y, r in year.items():
        new_dict[int(y)] = r
    new[date] = new_dict.copy()

p = Program(new)

"""
print("///////////////////////////")
print(p.globalMaxima())
print(p.globalMinima())
print(p.monthMaxima(11))
print(p.monthMinima(2))
print("///////////////////////////")
print(p.monthMaximumDerivate(2))
print(p.monthMinimumDerivate(2))
print(p.globalMaximumDerivative())
print(p.globalMinimumDerivative())
print("///////////////////////////")
date = Date(1, 1, 2000, 2024)
date.stefiho_loadData(json_data, p.measurements)
print(p.day_variences(date))
"""
date = Date(20, 1, 2000, 2024)
date.stefiho_loadData(json_data, p.measurements)

print(p.get_lore(date))
