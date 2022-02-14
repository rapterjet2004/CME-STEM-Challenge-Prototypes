import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

data = pd.read_csv(r'C:\Users\juliu\PythonProjects\gme_stock_data.csv')
xraw = data["Date"]
y = data["High"]

x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in xraw]

plt.plot(x, y ,c= "green")
plt.xlabel("Month")
plt.ylabel("Highest Price")
plt.show()