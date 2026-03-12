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

 
    median_temp = numpy.median(temperatures)
    humidity_median=numpy.median(humidity)
    wind_median = numpy.median(wind)
    precipitation_median=numpy.median(precipitation)


    mode_result = stats.mode(temperatures, keepdims=True)
    most_common_temp = float(mode_result.mode[0])

    average_humidity = numpy.mean(humidity)
    average_wind = numpy.mean(wind)
    average_temp = numpy.mean(temperatures)
    
    plt.plot(temperatures, marker="o", markersize=4, color="#e41a1c", label="Temperature °C")  # röd
    plt.plot(humidity, marker="o", markersize=4, color="#377eb8", label="Humidity %")         # blå
    plt.plot(wind, marker="o", markersize=4, color="#4daf4a", label="Wind speed m/s")          # grön
    plt.plot(precipitation, marker="o", markersize=4, color="#ff7f00", label="Precipitation mm")  # orange

# Horisontella linjer (matchande färger med linjer)
    plt.axhline(y=average_temp, color="#e41a1c", linestyle="--", label=f"Average Temp: {average_temp:.1f} °C")
    plt.axhline(y=median_temp, color="#e41a1c", linestyle=":", label=f"Median Temp: {median_temp:.1f} °C")
    plt.axhline(y=most_common_temp, color="#e41a1c", linestyle="-.", label=f"Most Frequent Temp: {most_common_temp:.1f} °C")

    plt.axhline(y=average_humidity, color="#377eb8", linestyle="--", label=f"Average Humidity: {average_humidity:.1f} %")
    plt.axhline(y=humidity_median, color="#377eb8", linestyle=":", label=f"Median Humidity: {humidity_median:.1f} %")

    plt.axhline(y=average_wind, color="#4daf4a", linestyle="--", label=f"Average Wind: {average_wind:.1f} m/s")
    plt.axhline(y=wind_median, color="#4daf4a", linestyle=":", label=f"Median Wind: {wind_median:.1f} m/s")

    plt.axhline(y=precipitation_median, color="#ff7f00", linestyle="--", label=f"Median Precipitation: {precipitation_median:.1f} mm")
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