import datetime
from time import sleep
import os

f = open("bell_time.txt", 'r')	#open file

time = []						#blank list

while(True):
	line = f.readline()[:-1]
	tmp = line.split('.')
	time.append(tmp)
	if not line: break			#time = [[hh, mm], [hh, mm], [hh,mm]]

while(True):
	dt = datetime.datetime.now()

	for i in range(0, len(time)-1):
		if(dt.hour == int(time[i][0])):
			if(dt.minute == int(time[i][1])):		#compare with current time
				os.system("start ./music.mp3")		#ring bell
				sleep(60)
	sleep(2)

f.close()		#close file