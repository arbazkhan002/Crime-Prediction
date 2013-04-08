#~ IncidntNum,Category,Descript,DayOfWeek,Month,Day,Year,Hours,Minute,PdDistrict,Resolution, Street, bin
#~ "/" replaced with "--"
f=open("new_data.csv")
dictn={}
for line in f:
	l = line.strip().split(",")
	bins=l[12]
	if bins!="":
		if bins not in dictn:
			dictn[bins]=[]
			print repr(bins)
		dictn[bins].append(line)	
f.close()
for key in dictn:
	f= open("PD/"+key,"w")		
	for line in dictn[key]:
		f.write(line)
	f.close()	
