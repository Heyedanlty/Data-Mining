import matplotlib.pyplot as plt
import numpy as np

def show(P):

    x = []
    y1 = []
    y2 = []
    y3 = []


    for i in range(96):
        x.append(i)
        y1.append(P[0,i])
        y2.append(P[1,i])
        y3.append(P[2,i])


    plt.plot(x,y1)
    plt.plot(x,y2)
    plt.plot(x,y3)

    plt.plot()

    plt.show()