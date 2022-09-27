
from matplotlib import pyplot as plt
import PrettyUglyPlot

y=[year2019,
year2020,
year2021,
year2022]

x=['2019','2020','2021','2022']

area=[6500/5,7700/5,8200/5,8600/5]

#### Pretty Plot #####

colors='orange'

ax = plt.axes()
ax.set_facecolor("#C6E7FF")
plt.scatter(x, y, s=area, c=colors)#,alpha=0.5)

plt.xlabel("Years",fontdict = {'fontsize' : 20})
plt.ylabel("Wind Speed (MPH)",fontdict = {'fontsize' : 20})
plt.title("Average Yearly Wind Speed",fontdict = {'fontsize' : 35})
plt.show()


##### Ugly Plot #####


area=[6500/2,7700/2,8200/2,8600/2]
colors='green'

ax = plt.axes()
ax.set_facecolor("maroon")
plt.scatter(x, y, s=area, c=colors,alpha=0.5)

plt.xlabel("Years",fontdict = {'fontsize' : 20})
plt.ylabel("Wind Speed (MPH)",fontdict = {'fontsize' : 20})
plt.title("Average Yearly Wind Speed",fontdict = {'fontsize' : 35})
plt.show()

