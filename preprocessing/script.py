#~ IncidntNum,Category,Descript,DayOfWeek,Date,Time,PdDistrict,Resolution,Location,X,Y

#~  Range of latitudes
X=(-122.51364359485, -122.365246233094)

#~  Range of longitudes
Y=(37.7080162257804, 37.8180716693477)
deltaX = 0.14839736175599683
deltaY = 0.11005544356730468
intX = deltaX/30
intY = deltaY/30
f = open("clean_data_temp.csv")
g = open("new_data.csv","w")
for line in f:
	l=line.strip().split(",")
	try:
		x=float(l[-2])
		y=float(l[-1])
	except:
		print line	
	binX = int((x-X[0])/intX)
	if binX==30:		#Boundary case
		binX=29
	binY = int((y-Y[0])/intY)
	bins = binX*30+binY
	g.write(",".join(l[:-2])+","+str(bins)+"\n")
