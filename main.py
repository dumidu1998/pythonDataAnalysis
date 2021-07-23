import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk



df = pd.read_excel ('data.xls')

def Line():
    new = df.to_numpy()

    X = new[0][1:5]
    art = new[1][1:]
    mgt = new[2][1:]
    med = new[3][1:]
    sci = new[4][1:]

    X_axis = np.arange(len(X))
    x = new[0][1:7]
    y = [3, 3, 3, 3, 3, 3]

    # plot lines
    plt.plot(x, art, label="Art", linestyle="-")
    plt.plot(x, mgt, label="Management", linestyle="--")
    plt.plot(x, med, label="Medicine", linestyle="-.")
    plt.plot(x, sci, label="Science", linestyle=":")
    plt.legend()
    plt.show()

def Column():
    new = df.to_numpy()
    print(new[0][1:5])

    X = new[0][1:5]

    art = new[1][1:5]
    mgt = new[2][1:5]
    med = new[3][1:5]
    sci = new[4][1:5]

    X_axis = np.arange(len(X))

    plt.bar(X_axis - 0.1, art, 0.2, label='ART')
    plt.bar(X_axis + 0.1, mgt, 0.2, label='Management')
    plt.bar(X_axis + 0.3, med, 0.2, label='Medicine')
    plt.bar(X_axis + 0.5, sci, 0.2, label='Science')

    plt.xticks(X_axis, X)
    plt.xlabel("Year")
    plt.ylabel("Number of Students")
    plt.legend()
    plt.show()


def Pie():
    new = df.to_numpy()
    print(new[0][1:5])
    # print(new)

    X = new[0][1:5]

    art = new[1][6]
    mgt = new[2][6]
    med = new[3][6]
    sci = new[4][6]

    X_axis = np.arange(len(X))

    activities = ['Art', 'Management', 'Medical', 'Science']

    # portion covered by each label
    slices = [art, mgt, med, sci]

    # color for each label
    colors = ['r', 'y', 'g', 'b']

    # plotting the pie chart
    plt.pie(slices, labels=activities, colors=colors,
            startangle=90, shadow=True, explode=(0, 0, 0.1, 0),
            radius=1.2, autopct='%1.1f%%')

    plt.show()



