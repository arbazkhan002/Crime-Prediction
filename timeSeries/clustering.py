#~ IncidntNum,Category,Descript,DayOfWeek,Month,Day,Year,Hours,Minute,PdDistrict,Resolution, Street, bin
#~ "/" replaced with "--"
import os



#~ 1. Run this to get binwise count of crimes violent
DIR="Bin"
RESULTDIR = "results" 
r = open(RESULTDIR+"/clustering","w")

#~ tot_count=0
#~ hours = [0 for i in range(48)]
bins = [0 for i in range(900)]
Crimes = ['LARCENY--THEFT','ASSAULT', 'BURGLARY', 'KIDNAPPING', 'SUICIDE','ARSON', 'DRUG--NARCOTIC', 'VANDALISM', 'SEX OFFENSES- FORCIBLE', 'WEAPON LAWS','DISORDERLY CONDUCT']
#~ print Crimes
for File in os.listdir(DIR):
	f = open(DIR+"/"+File)
	for line in f:
		l=line.strip().split(",")		
		if l[1] in Crimes:
			bins[int(File)]+=1

for i in range(len(bins)):
	r.write(",".join([str(i/30),str(i%30),str(bins[i])])+"\n")
	

"""
RESULTDIR = "results" 
f = open(RESULTDIR+"/clustering")
r = open(RESULTDIR+"/clustering_norm.csv","w")
for line in f:
	l=line.strip().split(",")
	x=int(l[0])
	y=int(l[1])
	z=float(int(l[2]))
	r.write(",".join( map(str,[x,y,z]) ) + "\n" )
	
"""	
	
	
