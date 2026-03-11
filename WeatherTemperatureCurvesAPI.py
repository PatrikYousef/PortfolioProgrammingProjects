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
    City(2, "Gothenburg", 57.707, 11.967),
    City(3, "Malmo", 55.606, 13.001),
    City(4, "Uppsala", 59.859, 17.639),
    City(5, "Linkoping", 58.411, 15.622),
    City(6, "Orebro", 59.274, 15.207),
    City(7, "Vasteras", 59.616, 16.553),
    City(8, "Umea", 63.828, 20.260),
    City(9, "Jonkoping", 57.781, 14.156),
    City(10, "Helsingborg", 56.047, 12.694),
    City(11, "Norrkoping", 58.594, 16.183),
    City(12, "Lund", 55.705, 13.191),
    City(13, "Gavle", 60.675, 17.142),
    City(14, "Sodertalje", 59.196, 17.625),
    City(15, "Vaxjo", 56.878, 14.809)
]

def printIDAndCityName():
    for city in cities:
        print(city.iden, city.namn)


def CitySystem():
    idstate = int(input("Enter the city id: "))

    # Find the city
    selected_city = next((city for city in cities if city.iden == idstate), None)

    if not selected_city:
        print("City not found")
        return

    # Request weather data
    url = f"https://api.open-meteo.com/v1/forecast?latitude={selected_city.lat}&longitude={selected_city.lon}&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m,precipitation"

    response = requests.get(url)
    data = response.json()

    temperatures = data["hourly"]["temperature_2m"]
    humidity = data["hourly"]["relative_humidity_2m"]
    wind = data["hourly"]["wind_speed_10m"]
    precipitation = data["hourly"]["precipitation"]

    print(f"Hourly weather data for {selected_city.namn}")

 
    average_temp = numpy.mean(temperatures)
    median_temp = numpy.median(temperatures)
    mode_result = stats.mode(temperatures, keepdims=True)
    most_common_temp = float(mode_result.mode[0])

    average_humidity = numpy.mean(humidity)
    average_wind = numpy.mean(wind)
    total_rain = numpy.sum(precipitation)

    print(f"Average temperature: {average_temp:.1f} °C")
    print(f"Median temperature: {median_temp:.1f} °C")
    print(f"Most frequent temperature: {most_common_temp:.1f} °C")

    print(f"Average humidity: {average_humidity:.1f} %")
    print(f"Average wind speed: {average_wind:.1f} m/s")
    print(f"Total precipitation: {total_rain:.1f} mm")


    plt.plot(temperatures, marker="o", markersize=4, color="blue", label="Temperature °C")
    plt.plot(humidity, marker="o", markersize=4, color="black", label="Humidity %")
    plt.plot(wind, marker="o", markersize=4, color="orange", label="Wind speed m/s")
    plt.plot(precipitation, marker="o", markersize=4, color="green", label="Precipitation mm")


    plt.axhline(y=average_temp, color="red", label=f"Average temp: {average_temp:.1f} °C")
    plt.axhline(y=median_temp, color="purple", label=f"Median temp: {median_temp:.1f} °C")
    plt.axhline(y=most_common_temp, color="cyan", label=f"Most frequent temp: {most_common_temp:.1f} °C")

    plt.xlabel("Time (hours)")
    plt.ylabel("Weather values")
    plt.title(f"Hourly weather data for {selected_city.namn}")
    plt.grid()
    plt.legend()

    plt.show()


def main():
    printIDAndCityName()
    CitySystem()
main()