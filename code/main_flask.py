from flask import Flask, request
from random import randrange

app = Flask("Weather lorAI")


@app.route("/", methods=["POST"])
def main():
    if request.method == "POST":
        date = request.args.to_dict()["date"]
        if randrange(2) == 0:
            return f"When Zoltan's heavens don a cloudy attire, prepare for Albert's day to set the air on fire.\n{date}"
        else:
            return f"When Martin's namesday comes to call, expect a warmth that never falls.\n{date}"


