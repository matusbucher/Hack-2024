from flask import Flask, request
import main
from json import loads

app = Flask("Weather lorAI")


@app.route("/", methods=["GET"])
def main():
    if request.method == "GET":
        date = request.args.to_dict()["date"]

        j = open("data/model_data1.json", "r")
        json_data = loads(j.read())
        data = {}
        tmp = {}
        for date, year in json_data.items():
            for y, r in year.items():
                tmp[int(y)] = r
            data[date] = tmp.copy()

        program = main.Program(data)
        lore = program.get_lore(main.Date(13, 7, 2000, 2024).loadData(data, *program.measurements))

        return f"{lore}"
