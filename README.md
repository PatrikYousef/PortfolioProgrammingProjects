# Growth Model

A Python program that visualizes height development over time using a growth curve model.

## Overview

This project lets you:

* Input your height and age
* Input your parents' heights
* Estimate your final height
* Visualize your growth against standard curves
* Track changes over time

The model uses cubic spline interpolation to generate smooth growth curves.

---

## Features

* Personal height tracking
* Parent-based height prediction
* Growth difference calculation
* Standard growth curve comparison
* Visual graph using matplotlib
* Multiple data points over time

---

## How It Works

### Input

You provide:

* Your current height
* Your age
* Your mother's height
* Your father's height

### Prediction

The program estimates final height using:

```
(mother + father + 13) / 2
```

This formula applies to boys.

### Growth Curves

* A reference curve is defined for a 180 cm individual
* The curve is scaled to create multiple height trajectories
* Your data is plotted against these curves

---

## Requirements

Install dependencies:

```
pip install matplotlib numpy scipy
```

---

## How to Run

Run the program:

```
python3 your_file_name.py
```

---

## Output

The program displays:

* Your growth over time
* Your parents' heights
* Predicted final height
* Standard growth curves
* Growth phases:

  * Rapid growth (age 11 to 15)
  * Slowing growth (age 15 to 18)

---

## Limitations

* The prediction formula is simplified
* Only accurate for general estimates
* Does not account for genetics beyond parents
* Assumes standard growth patterns

---

## Future Improvements

* Add support for girls
* Save data to file
* Build a web interface with Streamlit
* Add multiple user profiles
* Improve prediction accuracy

---

## License

Free to use and modify.
