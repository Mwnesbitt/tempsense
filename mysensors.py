#!/usr/bin/python3
#Mark Nesbitt
#20170829

import subprocess
import re
import datetime

#There's got to be a better way of doing this than my ugly re...

def main():
    sensors = subprocess.check_output("sensors").decode(encoding='UTF-8')
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    match = re.search('(acpitz-virtual-0)\s*(Adapter:\sVirtual\sdevice)\s(temp1:)\s*(\S+)\s+(\(.+?\))\s(temp2:)\s*(\S+)\s+(\(.+?\))\s(temp3:)\s*(\S+)\s+(\(.+?\))',str(sensors))
    firstdev = match.group(1)+match.group(2)
    dat1 = match.group(3)+"~"+match.group(4)+"~"+match.group(5)
    dat2 = match.group(6)+"~"+match.group(7)+"~"+match.group(8)
    dat3 = match.group(9)+"~"+match.group(10)+"~"+match.group(11)
    print(timestamp+"~"+firstdev+"~"+dat1)
    print(timestamp+"~"+firstdev+"~"+dat2)
    print(timestamp+"~"+firstdev+"~"+dat3)

    match = re.search('(coretemp-isa-0000)\s*(Adapter:\sISA\sadapter)\s(Physical\sid\s0:)\s*(\S+)\s+(\(.+?\))\s(Core\s0:)\s*(\S+)\s+(\(.+?\))\s(Core\s1:)\s*(\S+)\s+(\(.+?\))',str(sensors))
    seconddev = match.group(1)+match.group(2)
    dat1 = match.group(3)+"~"+match.group(4)+"~"+match.group(5)
    dat2 = match.group(6)+"~"+match.group(7)+"~"+match.group(8)
    dat3 = match.group(9)+"~"+match.group(10)+"~"+match.group(11)
    print(timestamp+"~"+seconddev+"~"+dat1)
    print(timestamp+"~"+seconddev+"~"+dat2)
    print(timestamp+"~"+seconddev+"~"+dat3)



if __name__ == '__main__':
    main()
