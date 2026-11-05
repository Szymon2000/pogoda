

import requests

#API_KEY = "573385d6e51092b0bddedced045d3282"
#CITY = "Lisbon"

#print(data)

import requests
from datetime import datetime
from common.functions import k_to_c, ms_to_kmh
from common.config import AppConfig

API_KEY = AppConfig.API_KEY
CITY = AppConfig.CITY

def get_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    weather = {
        "temperatura": k_to_c(data.get("main").get("temp")),
        "miejsce": data.get("name"),"temp_odczuwalna": k_to_c(data.get("main").get(("feels_like"))),
        "cisnienie": data.get("main").get("pressure"), "wilgotnosc": data.get("main").get("humidity"),
        "predkosc wiatru": ms_to_kmh(data.get("wind").get("speed")), "zachmurzenie" : data.get("clouds").get("all"),
        "wschód": datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%H:%M"), "zachód": datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M"),




    }

    return(weather)