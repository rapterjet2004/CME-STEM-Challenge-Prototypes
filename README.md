# CME STEM Challenge Prototypes
includes proof of concept apps, test apps, and experiments

# tKinter, CSV, and Matplot lib test app
uses GME stock data downloaded off of yahoo finance
<img width="708" alt="matplotlib-gme-csv-test" src="https://user-images.githubusercontent.com/69230048/153903853-3dcf7b26-547f-456c-8d9e-7243098f7470.PNG">

# tkinter, pyTrends, and matplot lib test app
gathers historical google search trends data using the pyTrends API

<img width="478" alt="matplotlib-pytrends-test" src="https://user-images.githubusercontent.com/69230048/153904247-9a3aa6d3-67e0-41f4-acc6-47c25275011f.PNG">

# Combined pyTrends and CSV tKinter application
Gathers and displays both graphs in tKinter window, on button press

<img width="679" alt="matplotlib-gme-pytrends-tkinter-test" src="https://user-images.githubusercontent.com/69230048/153904668-15b19b6a-52ab-4182-b39b-6efa2ff68474.PNG">

# tKinter Designer API test
Behold the power of good lighting and iPhone Filters. tKinter is ugly as a molerat, this makes it look better. Uses the web based Figma as a designer for the GUI, data is translated into tKinter using the tKinter Designer API
documentation found <a href="https://github.com/ParthJadhav/Tkinter-Designer/blob/master/docs/instructions.md#using-cli ">here</a>

<img width="601" alt="figma-tKinter-test" src="https://user-images.githubusercontent.com/69230048/153905281-5ad719f7-85ab-458c-963c-843156a234c2.PNG">

# tKinter Designer test GUI dashbaord
This is a prototype/proof of concept idea for what our final application would look like. It's a simple dashboard, buttons nonfunctional. The top Line graph is GME stock, the bottom is google search trends using pytrends. The piechart is a dummy chart. We might make the application a single page application only, to reduce complexity.

<img width="747" alt="image" src="https://user-images.githubusercontent.com/69230048/155898560-930d46ba-3c13-4df5-bebd-957887bc58cf.png">

# Backtrader Library for performing technical analysis on data
Backtrader is a fantastic python library for performing technical analysis on financial data. It allows us to program custom strategies and indicators for use in predicting financial prices using the Cerebros engine. It also has a bit of steep learning curve and some boring as idaho <a href="https://www.backtrader.com/docu/">documentation</a>. Here is a matplotlib plot of the Bitcoin data CME sent us graphed using Backtraders inbuild plot() function. Note, the crossover strategy used here performs best during periods of low volatility, which is bitcoin isn't really known for. I manually set the time period to start past the big mountain.
<img width="960" alt="image" src="https://user-images.githubusercontent.com/69230048/155910854-855d5791-b154-4b91-a50e-c33fef42638c.png">

looks cool right, I believe I made a profit of about 1000 in the adjusted time interval. Using the entire time interval I lost about 4k using the same strategy.
