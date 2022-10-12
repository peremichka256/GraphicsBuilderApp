import tkinter
from tkinter import *
from tkinter import ttk
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import pandas as pd
matplotlib.use("TkAgg")


def graphic_build_click():
    table = pd.read_excel('parabola.xlsx')
    x = table.values[:, 0]
    y = table.values[:, 1]
    graphic_figure = plt.figure(figsize = (7, 7))
    graphic_figure.add_subplot(111)
    canvas = FigureCanvasTkAgg(graphic_figure, root)
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack()
    plt.plot(x, y)


if __name__ == '__main__':
    root = Tk()
    root.title("Graphic build")
    root.geometry('500x500+0+0')
    root.resizable(False, False)
    build_button = ttk.Button(text = "Построить график",
                              command = graphic_build_click)
    build_button.pack(anchor = CENTER)
    root.mainloop()
