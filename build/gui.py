
from json import load
from time import sleep
from threading import Thread 
from cgitb import text
from pathlib import Path
from tkinter import *
from turtle import left
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from pytrends.request import TrendReq
from matplotlib.figure import Figure

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.geometry("1000x600")
window.configure(bg = "#373737")
frame_1 = Frame(master=window, width=1000, height=600)
frame_1.pack()

canvas = Canvas(
    frame_1,
    bg = "#373737",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    100.0,
    600.0,
    fill="#488F36",
    outline="")



canvas.create_text(
    125.0,
    0.0,
    anchor="nw",
    text="Dashboard",
    fill="#FFFFFF",
    font=("Roboto", 48 * -1)
)

canvas.create_text(
    11.0,
    60.0,
    anchor="nw",
    text="Dashboard",
    fill="#FFFFFF",
    font=("Roboto", 15 * -1)
)

canvas.create_text(
    11.0,
    107.0,
    anchor="nw",
    text="Real Time",
    fill="#FFFFFF",
    font=("Roboto", 15 * -1)
)

canvas.create_text(
    11.0,
    154.0,
    anchor="nw",
    text="Settings",
    fill="#FFFFFF",
    font=("Roboto", 15 * -1)
)

canvas1 = Canvas(
    canvas,
    bg = "white",
    height = 200,
    width = 600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas1.place(x=125,y=70)

canvas2 = Canvas(
    canvas,
    bg = "white",
    height = 200,
    width = 600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas2.place(x=125,y=300)

canvas3 = Canvas(
    canvas,
    bg = "white",
    height = 200,
    width = 200,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas3.place(x=750,y=70)



def plot_graph1():
    fig = Figure(figsize = (6, 2), dpi = 100)
    fig.patch.set_facecolor('#484848')
    data = pd.read_csv(r'C:\Users\juliu\PythonProjects\gme_stock_data.csv')
    xraw = data["Date"]
    y = data["High"]
    x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in xraw]
    # adding the subplot
    plt = fig.add_subplot(111) #params stands for grid of 2x2, plot 1(top left)
    plt.plot(x, y ,c= "green")
    for label in plt.xaxis.get_ticklabels()[::2]:
        label.set_visible(False) 
    graph = FigureCanvasTkAgg(fig, master = canvas1)  
    graph.draw()
    # placing the canvas on the Tkinter window
    graph.get_tk_widget().pack()

def plot_graph2():
    fig = Figure(figsize = (6, 2), dpi = 100)
    fig.patch.set_facecolor('#484848')
    #make a pytrends object to request Google Trends data
    pytrends = TrendReq(hl='en-US')                     
    #extract data about weekly searches of certain keywords
    keywords = ["GME", "WallStreetBets", "AMC", "Shorting"]
    pytrends.build_payload(keywords, timeframe='today 5-y')
    #store kewords data
    data = pytrends.interest_over_time()
    data = data.drop('isPartial', axis=1)
    plt = fig.add_subplot(111)
    plt.plot(data)
    graph = FigureCanvasTkAgg(fig, master = canvas2)  
    graph.draw()
    # placing the canvas on the Tkinter window
    graph.get_tk_widget().pack()

def plot_graph3():
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [15, 30, 45, 10]
    explode = (0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig = Figure(figsize = (2, 2), dpi = 100)
    fig.patch.set_facecolor('#484848')
    plt = fig.add_subplot(111)
    plt.pie(sizes,shadow=True, startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    graph = FigureCanvasTkAgg(fig, master = canvas3)  
    graph.draw()
    graph.get_tk_widget().pack()

plt.style.use("dark_background")
plot_graph1()
plot_graph2()
plot_graph3()
window.resizable(False, False)
window.mainloop()
