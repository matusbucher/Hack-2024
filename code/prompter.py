import openai
from json import loads
from random import randrange

API_KEY = ""  # insert key here
client = openai.OpenAI(api_key=API_KEY)

MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]


def get_nameday(date) -> str:
    with open("namedays.json", "r") as file:
        return loads(file.read())[date]


#  TODO word limits
#  TODO features, extra rhymes, puns
class LoreGenerator:
    def __init__(self, day: str):
        self.day = day
        self.name = get_nameday(day)

    def get_ai_response(self, prompt) -> str:
        prompt += " DO NOT use more than 30 words."

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return completion.choices[0].message.content

    def prompt_growth_extreme(self, attribute, is_rising, is_period_year):
        attribute_names = {"cloud_cover": "amount of clouds",
                           "temperature": "temperature",
                           "wind_speed": "amount of wind",
                           "rain_mm": "amount of rain",
                           "snow_mm": "amount of snow"}

        text = attribute_names[attribute]

        if is_rising:
            direction = "rise"
        else:
            direction = "decrease"

        if is_period_year:
            prompt = f"Give me a short weather lore expressing that after the day of {self.name}'s nameday ({self.day}), the {text} should {direction} drastically, it is the most intense {direction} of the whole year. Be creative, do not use the word nameday."
        else:
            prompt = f"Give me a short weather lore expressing that after the day of {self.name}'s nameday ({self.day}), the {text} should {direction} drastically, be creative, do not use the word nameday."
        return self.get_ai_response(prompt)

    def prompt_extreme(self, attribute, is_period_year: bool, is_maximum: bool) -> str:
        max_attribute_texts = {"cloud_cover": "is the least sunny one",
                               "temperature": "is the hottest",
                               "wind_speed": "is the windiest",
                               "rain_mm": "is the rainiest",
                               "snow_mm": "is the snowiest"}
        min_attribute_texts = {"cloud_cover": "is the sunniest",
                               "temperature": "is the coldest",
                               "wind_speed": "is the least windy",
                               "rain_mm": "is the least rainy",  # nedava zmysel
                               "snow_mm": "is the least snowy"}  # nedava zmysel

        if is_period_year:
            time = "the year"
        else:
            time = MONTHS[int(self.day[3:-1])]

        if is_maximum:
            text = max_attribute_texts[attribute]
        else:
            text = min_attribute_texts[attribute]

        prompt = f"Give me a short weather lore expressing the fact, that the day of {self.name}'s nameday {text} in {time},  be creative, do not use the word nameday."
        return self.get_ai_response(prompt)

    def prompt_variability(self, attribute, is_high, value) -> str:
        attribute_names = {"cloud_cover": "amount of clouds",
                           "temperature": "temperature",
                           "wind_speed": "speed of wind",
                           "rain_mm": "amount of rain",
                           "snow_mm": "amount of snow"}

        values_formatted = {"cloud_cover": f"covering around {int(value * 10)}%of the sky",
                           "temperature": f"around {value} degrees celsius",
                           "wind_speed": f"with speed around {round(value * 1.852, 2)} kmh",
                           "rain_mm": f"around {value} mm",
                           "snow_mm": f"around {value} mm"}
        if is_high:
            prompt = f"Give me a short weather lore, base on the fact, that the {attribute_names[attribute]} is extremely unpredictable on the day of {self.name}'s nameday. Be creative, do not use the word nameday."
        else:
            prompt = f"Give me a short weather lore, base on the fact, that the {attribute_names[attribute]} is extremely stable on the day of {self.name}'s nameday, {values_formatted[attribute]}. Be creative, do not use the word nameday."
        return self.get_ai_response(prompt)

    def prompt_correlation_pair(self, attribute1, attribute2, other_date, positive_correlation: bool, time_period) -> str:
        #  time_period: 0 for day, 1 for month, 2 for year
        attributes_first = {"cloud_cover": "is cloudy", "temperature": "is hot", "wind_speed": "is windy",
                            "rain_mm": "rains", "snow_mm": "snows"}

        if positive_correlation:
            attributes_second = {"cloud_cover": "be cloudy", "temperature": "be hot", "wind_speed": "be windy",
                                 "rain_mm": "rain", "snow_mm": "snow"}
        else:
            attributes_second = {"cloud_cover": "be sunny", "temperature": "be cold", "wind_speed": "not be windy",
                                 "rain_mm": "not rain", "snow_mm": "not snow"}

        if time_period == 0:
            time_name = f"on the day of {get_nameday(other_date)}'s nameday"
        elif time_period == 1:
            time_name = f"in the following {MONTHS[other_date]}"
        else:
            time_name = f"in the following year"

        prompt = f"Give me a short weather lore expressing that if it {attributes_first[attribute1]} on the day of " \
                 f"{self.name}'s namesday, {time_name} it will most likely {attributes_second[attribute2]}, be creative, do not use the word nameday."

        use_verses = randrange(5) == 0
        if use_verses:
            prompt += " Make it a four verse poem. Do not write more than four verses."
        prompt = prompt
        return self.get_ai_response(prompt)
