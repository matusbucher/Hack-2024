from json import dumps, loads
import unidecode

new = {}


with open("data/model_data1.json", "r", encoding="utf-8") as f:
    js = f.read()
    json_data = loads(js)
    f.close()

new = {}
new_dict = {}
for date, year in json_data.items():
    for y, r in year.items():
        new_dict[int(y)] = r
    new[date] = new_dict.copy()

print(new)

with open("data/new_model_data1.json", "w", encoding="utf-8") as j:
    j.write(dumps(new))
    j.close()