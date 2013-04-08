#~ Discretizes time
f = open("new_data.csv")
g = open("final_data.csv","w")
for line in f:
	l=line.strip().split(",")
	x=int(l[8])
	if x<30:
		x="00"
	else:
		x="30"	
	g.write(",".join(l[:8])+","+x+","+",".join(l[9:])+"\n")
