from dotenv import load_dotenv
import os
import requests
from pprint import pprint

load_dotenv()


def get_current_weather(city="Bangalore"):
    requests_url=f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("OPEN_WEATHER_API_KEY")}&q={city}&units=metric'
    weather_data = requests.get(requests_url).json()
    return weather_data
    
if __name__ == "__main__":
    print('\nGet Current Weather Condition')
    city = input("\Please enter a city name: ")    
    weather_data = get_current_weather(city)
    
    pprint(f'\n{weather_data}')