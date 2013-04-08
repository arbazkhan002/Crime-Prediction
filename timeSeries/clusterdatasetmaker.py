from datetime import date,datetime,timedelta
import os

DIR="clusters"
RESULTDIR = "clustersdataset" 

def getint(p):
	return ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"].index(p)

#~ Break up between the days which is set as attribute later
day_start = 7

for File in os.listdir(DIR):
	i=File
	r = open(RESULTDIR+"/cluster"+i+"train.csv","w")
	s = open(RESULTDIR+"/cluster"+i+"test.csv","w")
	r.write("dayno,dow,sums1,sums2,cc\n")
	s.write("dayno,dow,sums1,sums2,cc\n")
	tot_count=0
	dayarr = [0 for i in range(3561)]
	

	#~ for File in os.listdir(DIR):
	#~ File="0"	
	f = open(DIR+"/"+File)
	#~ print File
	start=datetime(2003,1,1)
	for line in f:
		l=line.split(",")
		month = int(l[4])
		day = int(l[5])
		year = int(l[6])
		dt=datetime(year,month,day)-start
		
		try:
			dayarr[dt.days]+=1
		except:
			print (datetime(year,month,day)-start).days, 365*9+2
			exit(0)
			
	for i in range(day_start,len(dayarr)):
		n=(date(2003,1,1)+timedelta(days=i)).weekday()
		#~ if i>30:
		#~ sums1=sum(dayarr[i-30:i])	
		#~ sums2=sum(dayarr[i-60:i-30])	
		sums2=sum(dayarr[i-day_start:i])	
		sums1=sum(dayarr[i-2*day_start:i-day_start])	
		if i<=365*9+2:	
			r.write(",".join(map(str,[i,n,sums1,sums2,dayarr[i]]))+"\n")
		else:
			s.write(",".join(map(str,[i,n,sums1,sums2,dayarr[i]]))+"\n")
	r.close()
	s.close()	
