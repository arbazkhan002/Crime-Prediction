#~ IncidntNum,Category,Descript,DayOfWeek,Month,Day,Year,Hours,Minute,PdDistrict,Resolution, Street, bin
#~ "/" replaced with "--"
import os

DIR="Crime"


RESULTDIR1 = "RESULTS" 
r = open(RESULTDIR1+"/pdcrimeday","w")
for File in os.listdir(DIR):
	if "PORNO" in File:
		continue
	#~ print os.listdir(DIR),"*"*12,File
	f=open(DIR+"/"+File)
	dictn={}
	for line in f:
		l = line.strip().split(",")
		bins=l[9]
		if bins!="":
			if bins not in dictn:
				dictn[bins]=[]
				print repr(bins)
			dictn[bins].append(line)	
	f.close()
	os.mkdir("CrimePD/"+File)
	for key in dictn:
		f= open("CrimePD/"+File+"/"+key,"w")		
		for line in dictn[key]:
			f.write(line)
		f.close()	



	#~ IncidntNum,Category,Descript,DayOfWeek,Month,Day,Year,Hours,Minute,PdDistrict,Resolution,bin
	#~ 00 -> 00 to 29 mins
	#~ 30 -> 30 to 59 mins
	#~ Find lift measure between two entities in a columnwise file

	DIR1="CrimePD/"+File

	
	tot_count=0
	hours = {}
	for F in os.listdir(DIR1):
		f = open(DIR1+"/"+F)
		for line in f:
			l = line.strip().split(",")
			
			h = (l[3])
			if h not in hours:
				hours[h]=0
			#~ print l,h	
			hours[h]+=1
			tot_count+=1
			
	for F in os.listdir(DIR1):
		f = open(DIR1+"/"+F)
		count = 0
		dictn = {}
		for line in f:
			l=line.strip().split(",")
			if l[3] not in dictn:
				dictn[l[3]]=0 
			dictn[l[3]]+=1
			count+=1		
		for key in dictn:				
			#~ print key,tot_count,count
			#~ try:
			r.write(File+","+F+","+str(key)+","+str(float(dictn[key]*tot_count)/(count*hours[key]))+"\n")		#in the end multiply with tot_count
			#~ except:
				#~ continue
