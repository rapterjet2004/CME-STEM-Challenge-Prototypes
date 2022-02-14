from pytrends.request import TrendReq
import matplotlib.pyplot as plt

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
plt.plot(data)

#add titles
plt.suptitle('Searches on Google Trends')
plt.xlabel('years')                       
plt.ylabel('weekly searches')  

#add legend
plt.legend(keywords, loc='upper left')

plt.show()
#plt.savefig('best_language.png')
