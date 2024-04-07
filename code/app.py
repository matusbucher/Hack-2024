from flask import Flask, request
from main import Program
from json import loads
from Date import Date

app = Flask("Weather lorAI")


@app.route("/", methods=["GET"])
def main():
    if request.method == "GET":
        date = request.args.to_dict()["date"]

        j = open("../data/model_data1.json", "r")
        json_data = loads(j.read())
        data = {}
        tmp = {}
        for d, year in json_data.items():
            for y, r in year.items():
                tmp[int(y)] = r
            data[d] = tmp.copy()

        program = Program(data)
        lore = program.get_lore(Date(int(date[:2]), int(date[3:-1]), 2000, 2024).loadData(data, *program.measurements))

        print(lore)

        return f"{lore[0]}&{lore[1].capitalize()}"
