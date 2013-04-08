import matplotlib.pyplot as plt
f=open("clusterass.csv")

colors=['lightblue','grey','orange','white','black','yellow','pink','brown','blue','red']
#~ plt.clf()
for line in f:
	l=line.strip().split(",")
	x=int(l[1])
	y=int(l[2])
	if x==20:
		print colors[int(l[4])]
	plt.plot([x],[y],marker='o',color=colors[int(l[4])])
#~ #~
#~ plt.plot([20],[19],marker='o',color='red') 
#~ plt.plot([20],[20],marker='o',color='red') 
#~ plt.plot([20],[21],marker='o',color='red') 
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("clusterassignments.png")	
#~ plt.clf()
