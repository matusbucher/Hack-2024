import requests

station = 11968

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

start = Date(1, 1, 1999)
end = Date(1, 2, 1999)

result = requests.get(f"https://www.ogimet.com/display_synops2.php?lang=en&lugar={station}&tipo=ALL&ord=REV&nil=SI&fmt=txt&ano={begin.year}&mes={begin.month}&day={begin.day}&hora=12&anof={end.year}&mesf={end.month}&dayf={end.day}&horaf=12&send=send")
with open("daco.txt") as f:
    
