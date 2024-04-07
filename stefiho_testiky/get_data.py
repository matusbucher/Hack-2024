import requests
import time

station = 11968

with open("data.txt", "w") as a:
    a.close()

with open("log.txt", "w") as a:
    a.close()


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

start = Date(1, 1, 2000)
end = Date(31, 1, 2000)

def get_one_month_raw(start: Date, end: Date, station: int) -> list[str]:
    sleep_time = 10
    result = requests.get(f"https://www.ogimet.com/display_synops2.php?lang=en&lugar={station}&tipo=ALL&ord=REV&nil=SI&fmt=txt&ano={start.year}&mes={start.month}&day={start.day}&hora=00&anof={end.year}&mesf={end.month}&dayf={end.day}&horaf=00&send=send")

    while "#Sorry, Your quota limit for slow queries rate has been reached" in result.text:
        time.sleep(sleep_time)
        with open("log.txt", "a") as l:
            l.write(f"{start.year}, {start.month}, {"#Sorry, Your quota limit for slow queries rate has been reached" in result.text}, slept for {sleep_time}\n")
            l.close()
        sleep_time += 10

        result = requests.get(f"https://www.ogimet.com/display_synops2.php?lang=en&lugar={station}&tipo=ALL&ord=REV&nil=SI&fmt=txt&ano={start.year}&mes={start.month}&day={start.day}&hora=00&anof={end.year}&mesf={end.month}&dayf={end.day}&horaf=00&send=send")
        

    with open("log.txt", "a") as l:
        l.write(f"{start.year}, {start.month}, {"#Sorry, Your quota limit for slow queries rate has been reached" in result.text}\n")
        l.close()

    raw: list[str] = result.text.split("#")[-1].split("=")
    new: list[str] = []
    for line in raw:
        if line.strip() == "":
            print(line)
            continue

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


def get_all(station: int) -> None:
    #result: list[str] = []

    for year in range(2023, 2024):
        print(year)
        for month in range(11, 12):
            # if month == 8:
            #    continue
            # time.sleep(30)
            #result.extend(get_one_month_raw(Date(1, month, year), Date(31, month, year), station))
            with open("new_data.txt", "a") as f:
                output = get_one_month_raw(Date(1, month, year), Date(31, month, year), station)
                for line in output:
                    f.write(line)
                    f.write("\n")
                f.close()

    #return result

get_all(11968)
