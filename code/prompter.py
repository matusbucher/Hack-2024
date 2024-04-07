import openai
from json import loads
from random import randrange

#  WARNING, uncommenting loses money
'''
client = openai.OpenAI(api_key="")

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system",
         "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
)
'''
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]


def get_nameday(date) -> str:
    with open("namedays.json", "r") as file:
        return loads(file.read())[date]


class Fakt:
    def __init__(self):
        pass


class LoreGenerator:
    def __init__(self, day: str):
        self.day = day
        self.lore = ""
        self.name = get_nameday(day)

    def get_ai_response(self, prompt):
        pass

    def prompt_growth_extreme(self, attribute, is_rising: bool, is_period_year: bool):
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

        return f"Give me a short weather lore expressing that after the day of {self.name}'s nameday ({self.day}), the {text} should {direction} drastically, be creative, do not use the word nameday."

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

        return f"Give me a short weather lore expressing the fact, that the day of {self.name}'s nameday {text} in {time},  be creative, do not use the word nameday."

    #  getting input {"temperature": (True, temp_value)} # True means low variability
    def prompt_variability(self, attribute, period, is_maximum: bool) -> str:
        attribute_names = {"cloud_cover": "",
                           "temperature": "",
                           "wind_speed": "",
                           "rain_mm": "",
                           "snow_mm": ""}

    def prompt_correlation_pair(self, attribute1, attribute2, other_date, positive_correlation: bool) -> str:
        #  attributes in form cloud_cover, temperature, wind_speed, rain_mm, snow_mm
        attributes_first = {"cloud_cover": "is cloudy", "temperature": "is hot", "wind_speed": "is windy",
                            "rain_mm": "rains", "snow_mm": "snows"}

        if positive_correlation:
            attributes_second = {"cloud_cover": "be cloudy", "temperature": "be hot", "wind_speed": "be windy",
                                 "rain_mm": "rain", "snow_mm": "snow"}
        else:
            attributes_second = {"cloud_cover": "be sunny", "temperature": "be cold", "wind_speed": "not be windy",
                                 "rain_mm": "not rain", "snow_mm": "not snow"}

        other_name = get_nameday(other_date)

        prompt = f"Give me a short weather lore expressing that if it {attributes_first[attribute1]} on the day of " \
                 f"{self.name}'s namesday, it will most likely {attributes_second[attribute2]} on the day of " \
                 f"{other_name}'s namesday, be creative, do not use the word nameday."

        use_verses = randrange(5) == 0
        if use_verses:
            prompt += " Make it a four verse poem."
        return prompt


generator = LoreGenerator("07.04.")

print(generator.prompt_correlation_pair("cloud_cover", "temperature", "08.04.", True))
print(generator.prompt_extreme("temperature", True, False))
print(generator.prompt_growth_extreme("rain_mm", False))
