from flask import Flask, request
from random import randrange
from time import sleep

app = Flask("Weather lorAI")


@app.route("/", methods=["GET"])
def main():
    if request.method == "GET":
        date = request.args.to_dict()["date"]
        if randrange(2) == 0:
            return f"When Zoltan's heavens don a cloudy attire, prepare for Albert's day to set the air on fire."
        else:
            return f"When Martin's namesday comes to call, expect a warmth that never falls."


