import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
from scipy.interpolate import CubicSpline

MyInfoHeight = []
MyExempleHeight=[]
MyInfoAge = []

def info():
    myheight = int(input("Enter My height: "))
    myage = int(input("Age: "))

    mom = int(input("Enter Moms Height: "))
    dad = int(input("Enter Dads Height: "))

    summan = round((mom + dad + 13) / 2)

    MyInfoHeight.append(myheight)
    MyExempleHeight.append(myheight)
    MyInfoAge.append(myage)

    return myheight, myage, mom, dad, summan


def sortingHeight(MyExempleHeight):
    sorted_heights = sorted(MyExempleHeight, reverse=True)

    if len(sorted_heights) < 2:
        return 0
    else:
        total = sorted_heights[0] - sorted_heights[1]
        return total

def Default_Curve_Each_Height(target_height=180):

    x_data = np.array([5,6,7,8,9,10,11,12,13,14,15,16,17,18])
    y_data = np.array([110,116,122,128,134,140,145,150,158,168,175,178,180,180])

    x = np.linspace(5, 18, 400)

    cs = CubicSpline(x_data, y_data)
    y_ref = cs(x)

    L_ref = 180

    f = y_ref / L_ref

    # ny kurva
    y_new = target_height * f

    return x, y_new

def StartCurve():

    while True:

        plt.style.use("seaborn-v0_8-talk")
        fig, ax = plt.subplots(figsize=(8, 5))

        x_ticks = [5,6,7,8,9,10,11,12,13,14,15,16,17,18]
        y_ticks = [100,110,120,130,140,150,160,170,180,190,200]

        my_height, my_age, mom, dad, predicted_height = info()
        total_growth = sortingHeight(MyExempleHeight)

        ax.plot(MyInfoAge, MyInfoHeight,
                color="#1D4ED8",
                marker="o",
                label="Your height")

        ax.scatter(18, mom,
                   color="#F59E0B",
                   s=70,
                   label="Mother")

        ax.scatter(18, dad,
                   color="#64748B",
                   s=70,
                   label="Father")

        ax.scatter(18, predicted_height,
                   color="#0F172A",
                   s=80,
                   label=f"Predicted final height {predicted_height}")

        ax.scatter(18, my_height,
                   color="#F97316",
                   s=80,
                   label=f"Growth {total_growth} cm")

        for h in [160, 170, 180, 190, 200]:
            x, y = Default_Curve_Each_Height(h)
            ax.plot(x, y, color="grey")

        ax.axvspan(15, 18,
                   color="red",
                   alpha=0.10,
                   label="Slowing growth")

        ax.axvspan(11, 15,
                   color="green",
                   alpha=0.10,
                   label="Rapid growth phase growing 20-30 cm")

        x_curve, y_curve = Default_Curve_Each_Height()
        ax.plot(x_curve, y_curve,
                color="black",
                linewidth=2,
                label="Standard curve")

        ax.set_xticks(x_ticks)
        ax.set_yticks(y_ticks)

        ax.set_xlabel("Age")
        ax.set_ylabel("Height (cm)")
        ax.set_title("Growth Model")

        ax.legend()
        ax.grid()

        plt.show()

        stop = input("Continue? (y/n): ")
        if stop.lower() != "y":
            break


StartCurve()