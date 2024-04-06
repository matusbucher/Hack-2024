import requests

station = 11968

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

start = Date(1, 1, 2000)
end = Date(31, 1, 2000)

def get_one_month_raw(start: Date, end: Date, station: int) -> list[str]:

    result = requests.get(f"https://www.ogimet.com/display_synops2.php?lang=en&lugar={station}&tipo=ALL&ord=REV&nil=SI&fmt=txt&ano={start.year}&mes={start.month}&day={start.day}&hora=12&anof={end.year}&mesf={end.month}&dayf={end.day}&horaf=12&send=send")

    raw: list[str] = result.text.split("#")[-1].split("=")
    new: list[str] = []
    for line in raw:
        if line.strip()[0].isnumeric():
            new.append(line.strip())

    new_new: list[str] = []
    for line in new:
        new_line = ""
        for char in line:
            if char.isalnum() or (char == " " and new_line[-1] != " "):
                new_line += char
        new_new.append(new_line)

    return new_new
