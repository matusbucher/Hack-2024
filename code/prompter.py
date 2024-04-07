import openai
from json import loads
from random import randrange


#  WARNING, uncommenting loses money
'''
client = openai.OpenAI(api_key="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")

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system",
         "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
)
'''


def get_nameday(date) -> str:
    with open("namedays.json", "r") as file:
        return loads(file.read())[date]


class Fakt:
    def __init__(self):
        pass


class TheDay:
    def __init__(self, day: str, fakt: Fakt):
        self.day = day
        self.lore = ""

        self.name = get_nameday(day)
        #  self.fact = self.get_weather_fact()  # maybe facts

    def set_weather_fact(self):
        pass

    def get_ai_response(self, name, fact_type, fact_atribute, second_name=""):
        pass

    def prompt_extreme(self, attribute, period, is_maximum: bool) -> str:
        pass

    #  getting input {"temperature": (True, temp_value)} # True means low variability
    def prompt_variability(self, attribute, period, is_maximum: bool) -> str:
        pass

    def prompt_correlation(self, attribute1, attribute2, other_date, positive_correlation: bool) -> str:
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


day = TheDay("07.04.", None)

print(day.prompt_correlation("cloud_cover", "temperature", "08.04.", True))
