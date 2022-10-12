# coding: utf-8
from tkinter import *
from tkinter import ttk
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd


def graphic_build_click():
    table = pd.read_excel('parabola.xlsx')
    x = table.values[:, 0]
    y = table.values[:, 1]

    plt.figure(figsize = (7, 7))
    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    root = Tk()
    root.title("Graphic build")
    root.geometry('500x500+0+0')
    root.resizable(False, False)
    build_button = ttk.Button(text = "Построить график",
                              command = graphic_build_click)
    build_button.pack(anchor = CENTER)
    root.mainloop()
