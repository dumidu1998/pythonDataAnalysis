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


