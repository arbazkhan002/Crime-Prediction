import matplotlib.pyplot as plt
f=open("plotter.csv")

x=[]
y=[]
c=0
for line in f:
	l=line.split()
	actual = int(l[1])
	pred = float(l[2])
	x.append(actual)	
	y.append(pred)	
	c+=1
#~ print range(c), 	
plt.plot(range(c),x,label="actual")
plt.plot(range(c),y, label= "predicted")
plt.xlabel("time series(days)")
plt.ylabel("Crime Intensity")
plt.legend()
plt.savefig("res_time.png")	
