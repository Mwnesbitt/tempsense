#!/usr/bin/python3
#Mark Nesbitt
#20170829

import sys
from matplotlib import pyplot as plt
import datetime

f = open("./sensors.log", 'r')
logdata = f.readlines()
f.close()

#print(logdata)
dates = []
core0temps = []
core1temps = []
for line in logdata:
    strdate = line[:line.index('~')]
    date = datetime.datetime.strptime(strdate, '%Y-%m-%d %H:%M:%S')
    if date not in dates:
        dates.append(date)
    if "Core 0" in line:
        index = line.find("Core 0:")
        core0temps.append(float(line[index+9:index+13]))
    if "Core 1" in line:
        index = line.find("Core 1:")
        core1temps.append(float(line[index+9:index+13]))
#print(dates)
#print(core0temps)
#print(core1temps)
cutoff = datetime.datetime.now() - datetime.timedelta(days=2)
dates48 = list(filter(lambda x: x>cutoff, dates))
core0temps48 = core0temps[-len(dates48):]
core1temps48 = core1temps[-len(dates48):]

plt.plot(dates48, core0temps48, dates48, core1temps48)
plt.show()

