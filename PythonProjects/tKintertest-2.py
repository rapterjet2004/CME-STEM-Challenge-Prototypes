from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from pytrends.request import TrendReq

def plot():
    # the figure that will contain the plot
    fig = Figure(figsize = (10, 10), dpi = 100)
    data = pd.read_csv(r'C:\Users\juliu\PythonProjects\gme_stock_data.csv')
    xraw = data["Date"]
    y = data["High"]
    x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in xraw]

    # adding the subplot
    plt = fig.add_subplot(211) #params stands for grid of 2x2, plot 1(top left)
    plt.plot(x, y ,c= "green")
    #plt.xlabel("Month")
    #plt.ylabel("Highest Price")

    # creating the Matplotlib toolbar
    #toolbar = NavigationToolbar2Tk(canvas,window)
    #toolbar.update()
  
    # placing the toolbar on the Tkinter window
    #canvas.get_tk_widget().pack()

    #make a pytrends object to request Google Trends data
    pytrends = TrendReq(hl='en-US')     
                    
    #extract data about weekly searches of certain keywords
    keywords = ["GME", "WallStreetBets", "AMC", "Shorting"]
    pytrends.build_payload(keywords, timeframe='today 5-y')

    #store kewords data
    data = pytrends.interest_over_time()
    data = data.drop('isPartial', axis=1)

    data.tail()

    #plot data
    plt = fig.add_subplot(212)
    plt.plot(data)

    canvas = FigureCanvasTkAgg(fig, master = window)  
    canvas.draw()
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()


# the main Tkinter window
window = Tk()
  
# setting the title 
window.title('Plotting in Tkinter')
  
# dimensions of the main window
window.geometry("500x500")
  
# button that displays the plot
plot_button = Button(master = window, command = plot,height = 2, width = 10,text = "Plot")
  
# place the button 
# in main window
plot_button.pack()
  
# run the gui
window.mainloop()