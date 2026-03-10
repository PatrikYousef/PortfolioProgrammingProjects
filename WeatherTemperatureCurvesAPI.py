from dataclasses import dataclass
import requests
from typing import List
import pandas as pd
import sys
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy
from scipy import stats

@dataclass
class City:
    iden: int
    namn: str
    lat: float
    lon: float

@dataclass
class WeatherData:
    city: City
    temperatures: List[float]

cities = [
    City(1, "Stockholm", 59.329, 18.069),
    City(2, "Göteborg", 57.707, 11.967),
    City(3, "Malmö", 55.606, 13.001),
    City(4, "Uppsala", 59.859, 17.639),
    City(5, "Linköping", 58.411, 15.622),
    City(6, "Örebro", 59.274, 15.207),
    City(7, "Västerås", 59.616, 16.553),
    City(8, "Umeå", 63.828, 20.260),
    City(9, "Jönköping", 57.781, 14.156),
    City(10, "Helsingborg", 56.047, 12.694),
    City(11, "Norrköping", 58.594, 16.183),
    City(12, "Lund", 55.705, 13.191),
    City(13, "Gävle", 60.675, 17.142),
    City(14, "Södertälje", 59.196, 17.625),
    City(15, "Växjö", 56.878, 14.809)
]


def printIDAndCityName():
    for city in cities:
        print(city.iden, city.namn)

def CitySystem():
    idstate = int(input("Skriv den id som du vill veta om: "))
    
    # Hitta staden
    selected_city = next((city for city in cities if city.iden == idstate), None)
    if not selected_city:
        print("Staden finns inte")
        return
    
    # Hämta temperaturdata från API
    url = f"https://api.open-meteo.com/v1/forecast?latitude={selected_city.lat}&longitude={selected_city.lon}&hourly=temperature_2m"
    response = requests.get(url)
    data = response.json()
    temperatures = data["hourly"]["temperature_2m"]

    print(f"Timtemperaturer för {selected_city.namn}:")
    
    # Beräkningar
    avergetemp = numpy.mean(temperatures)
    mediantemp = numpy.median(temperatures)
    mode_result = stats.mode(temperatures, keepdims=True)
    tempappearmost = float(mode_result.mode[0])  

    # Plotta graf
    plt.plot(temperatures, marker="o", markersize=4, color="blue", label="TimTemperatur")      # timtemperaturer i blå
    plt.axhline(y=avergetemp, color="red", linestyle='-', label=f"Average: {avergetemp:.1f}°C")   # medel i röd
    plt.axhline(y=mediantemp, color="purple", linestyle='-', label=f"Median: {mediantemp:.1f}°C") # median i lila
    plt.axhline(y=tempappearmost, color="cyan", linestyle='-', label=f"Most frequent: {tempappearmost:.0f}°C") # mest förekommande i turkos

    plt.xlabel("Tid (timmar)")
    plt.ylabel("Temperatur (°C)")
    plt.title(f"Timtemperaturer för {selected_city.namn}")
    plt.xticks(rotation=45)
    plt.grid()
    plt.legend()
    plt.show()

printIDAndCityName()
CitySystem()
