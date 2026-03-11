# PortfolioProgrammingProjects
# 🌦 Weather Data Analysis Project

## 📌 Overview

This project is a Python application that retrieves and analyzes hourly weather data for major Swedish cities using the Open Meteo API.

You select a city, the program downloads weather data, calculates statistics, and visualizes the results in a graph.

The analysis focuses on:

* Temperature
* Humidity
* Wind speed
* Precipitation

The program also calculates statistical values for temperature:

* Average temperature
* Median temperature
* Most frequent temperature

---

# ✨ Features

## 🏙 City Selection

The program contains a predefined list of **15 Swedish cities**.

Each city includes:

* Unique ID
* City name
* Latitude
* Longitude

Example cities available in the system:

* Stockholm
* Gothenburg
* Malmo
* Uppsala
* Linkoping
* Orebro
* Vasteras
* Umea

Users select a city by entering the corresponding **city ID**.

---

## 🌐 Weather Data Retrieval

Weather data is retrieved from the **Open Meteo API**.

API endpoint:

```
https://api.open-meteo.com/v1/forecast
```

The program fetches hourly values for:

* Temperature at 2 meters
* Relative humidity
* Wind speed at 10 meters
* Precipitation

---

## 📊 Data Analysis

The program performs statistical analysis using **NumPy** and **SciPy**.

### Temperature statistics

* Average temperature
* Median temperature
* Most frequent temperature

### Additional weather metrics

* Average humidity
* Average wind speed
* Total precipitation

All values are printed in the terminal.

---

## 📈 Data Visualization

The program uses **Matplotlib** to generate a graph showing hourly weather patterns.

The graph includes curves for:

* Temperature
* Humidity
* Wind speed
* Precipitation

Temperature statistics are displayed as horizontal lines:

* Average temperature
* Median temperature
* Most frequent temperature

This makes it easy to see weather trends and variations.

---

# 🛠 Technologies Used

This project uses the following technologies:

* Python 3
* Requests
* NumPy
* SciPy
* Matplotlib
* Dataclasses

These libraries handle:

* API communication
* Data analysis
* Data visualization

---

# ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/PatrikYousef/PortfolioProgrammingProjects.git
```

Navigate to the project directory:

```bash
cd PortfolioProgrammingProjects
```

Install dependencies:

```bash
pip install requests numpy scipy matplotlib pandas
```

---

# ▶ Running the Program

Run the Python script:

```bash
python main.py
```

### Program workflow

1. The program prints all available cities with their IDs.
2. The user selects a city by entering its ID.
3. Weather data is retrieved from the API.
4. Statistics are calculated.
5. A graph displays the hourly weather data.

---

# 🧾 Example Output

Example terminal output:

```
Average temperature: 12.3 °C
Median temperature: 12.0 °C
Most frequent temperature: 11.8 °C

Average humidity: 68 %
Average wind speed: 3.4 m/s
Total precipitation: 4.1 mm
```

A graph then appears showing hourly weather patterns.

---

# 📁 Project Structure

```
PortfolioProgrammingProjects
│
├── main.py
└── README.md
```

### Main Components

**City class**

Stores city information:

* ID
* Name
* Latitude
* Longitude

**CitySystem function**

Handles:

* City selection
* API requests
* Data analysis
* Graph generation

---

# 🎯 Learning Objectives

This project demonstrates practical programming concepts:

* Working with REST APIs
* Data analysis with Python
* Statistical calculations
* Data visualization
* Object oriented programming with dataclasses
