#~ IncidntNum,Category,Descript,DayOfWeek,Month,Day,Year,Hours,Minute,PdDistrict,Resolution,bin
#~ 00 -> 00 to 29 mins
#~ 30 -> 30 to 59 mins
#~ Find lift measure between two entities in a columnwise file
import os

DIR="PD"
RESULTDIR = "RESULTS" 
r = open(RESULTDIR+"/pdtime","w")

tot_count=0
hours = [0 for i in range(48)]
for File in os.listdir(DIR):
	f = open(DIR+"/"+File)
	for line in f:
		l = line.strip().split(",")
		
		h = 2*int(l[7])
		if int(l[8])>30:
			h = (h+1)
		#~ print l,h	
		hours[h]+=1
		tot_count+=1
		
for File in os.listdir(DIR):
	f = open(DIR+"/"+File)
	count = 0
	dictn = {}
	for line in f:
		l=line.strip().split(",")
		if l[7] not in dictn:
			dictn[l[7]]=[0,0] 
		if int(l[8])<30:
			dictn[l[7]][0]+=1
		else:
			dictn[l[7]][1]+=1	
		count+=1		
	for key in dictn:				
		r.write(File+","+str(key)+"00"+","+str(float(dictn[key][0]*tot_count)/(count*hours[2*int(key)]))+"\n")		#in the end multiply with tot_count
		r.write(File+","+str(key)+"30"+","+str(float(dictn[key][1]*tot_count)/(count*hours[2*int(key)+1]))+"\n")		#in the end multiply with tot_count
	
