#~ 2. Create the cluster folder
f=open("clusterass.csv")
dictn1={}
for line in f:
	l = line.strip().split(",")
	bins=l[4]
	if bins!="":
		if bins not in dictn1:
			dictn1[bins]=[]
			#~ print repr(bins)
		dictn1[(int(l[1])*30+int(l[2]))]=bins
		#~ print (int(l[1])*30+int(l[2]))	
f.close()
#~ for key in dictn:
	#~ f= open("clusters/"+key,"w")		
	#~ for line in dictn[key]:
		#~ f.write(line)
	#~ f.close()	

f= open("new_data.csv")
dictn={}
for line in f:
	l = line.strip().split(",")
	if l[12]=="732732":
		continue
	try:	
		bins=dictn1[int(l[12])]
	except:
		print repr(l[12]),dictn1[585]	
		exit(0)
	if bins!="":
		if bins not in dictn:
			dictn[bins]=[]
			print repr(bins)
		dictn[bins].append(line)	
f.close()

for key in dictn:
	f= open("clusters/"+key,"w")		
	for line in dictn[key]:
		f.write(line)
	f.close()	
