from collections import defaultdict
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

pio.renderers.default = 'iframe'
import matplotlib.pyplot as plt

#read the data set
df = pd.read_excel('NEW Wind DS.xlsx')

# Sorting ang re arranging the data w.r.t. month and year

df['drec'] = pd.to_datetime(df['DATE'], format='%Y-%m-%d')
df['Year'] = pd.DatetimeIndex(df['drec']).year
df['Month'] = pd.DatetimeIndex(df['drec']).month

avg = np.mean(df['AWND'])

#removing all the nan values
df2 = df[df[['Year', 'Month']].notnull().all(1)]

#print(df2['Season'])

#df.to_csv('output2.csv', encoding='utf-8')

d = defaultdict(list)
for key, value in zip(df2['Month'],df2['AWND']):
    d[key].append(value)

NewDictionary = dict(d)
#print(NewDictionary) #got a dictionary with month as key and value as AWND


# Arrays for storing the Avg wind data of the respective seasons
winter = []
spring = []
summer = []
fall = []

# assigning AWND to respective seasons
for i in NewDictionary.keys():
    if i==1 or i==2 or i==12 : # appending winter months AWND
        for j in NewDictionary[i]:
            winter.append(j)
    elif i==3 or i==4 or i==5 : # appending spring months AWND
        for j in NewDictionary[i]:
            spring.append(j)
    elif i==6 or i==7 or i==8 : # appending summer months AWND
        for j in NewDictionary[i]:
            summer.append(j)
    elif i==9 or i==10 or i==11 : # appending fall months AWND
        for j in NewDictionary[i]:
            fall.append(j)


## Yearly average speed calculations

yearlyAve= defaultdict(list)
for key, value in zip(df2['Year'],df2['AWND']):
    yearlyAve[key].append(value)

NewDictionaryYear = dict(yearlyAve)

# Arrays for storing the Avg wind data of the respective years
year2019 = np.mean(NewDictionaryYear[2019])
year2020 = np.mean(NewDictionaryYear[2020])
year2021 = np.mean(NewDictionaryYear[2021])
year2022 = np.mean(NewDictionaryYear[2022])


print(year2019, year2020,year2021,year2022,sep='\n')

## end

# Wind plot Computation

# for finding the average of the seasons - For wind speed one
avgWinter = np.mean(winter)
avgSpring = np.mean(spring)
avgSummer = np.mean(summer)
avgFall = np.mean(fall)
#print(avgWinter,avgSpring,avgSummer,avgFall,sep='\n')

##### Plotting Speed one ####

# On the next one

fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = 270,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Speed"}))

fig.show()

# Bar Plot Computation
# to find the monthly average
months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
monthlyMean={}
x=0
for i in NewDictionary.keys():
        avg = np.mean(NewDictionary[i])
        monthlyMean[months[x]]=avg
        x+=1

#print("Monthly mean = ",monthlyMean)

###### Plotting Bar Plot ######

#### Pretty Plot

months = list(monthlyMean.keys())
wind = list(monthlyMean.values())

#fig = plt.figure(figsize=(10, 5))
ax = plt.axes()
ax.set_facecolor("#C6E7FF")
#
# creating the bar plot
plt.bar(months, wind,color='orange',width=0.6)

plt.xlabel("Months",fontdict = {'fontsize' : 20})
plt.ylabel("Wind Speed (MPH)",fontdict = {'fontsize' : 20})
plt.title("Average Monthly Wind Speed",fontdict = {'fontsize' : 35})
plt.show()

##### Ugly Plot

ax = plt.axes()
ax.set_facecolor("purple")
#
# creating the bar plot
plt.bar(months, wind,color='green',width=0.6)

plt.xlabel("Months")
plt.ylabel("Wind Speed (MPH)")
plt.title("Average Monthly Wind Speed")

plt.xlim(1, 20)
plt.ylim(-298, 200)
plt.show()
