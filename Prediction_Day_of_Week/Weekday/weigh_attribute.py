#+=
import sys
import os
input_dir = "nominal_training_data/alldays/"
output_dir = "nominal_training_data/alldays_weighted/"
try:
	os.mkdir(output_dir)
except:
	pass
files = os.listdir(input_dir)

if len(sys.argv)==2:
	T = int(sys.argv[1])		# T-month approach
else:
	print "sys.argv is not 2."
	exit(1)

del_list = []
for filename in files:
	print "Filename:", filename
	fp_w = open(os.path.join(output_dir,filename),"w")
	fp_r = open(os.path.join(input_dir,filename))
	zeros = 0.0
	nonzeros = 0.0
	for i in xrange(5+T):
		fp_w.write(fp_r.readline())
	fp_w.write("@attribute weight numeric\n")
	for i in xrange(2):
		fp_w.write(fp_r.readline())
	while(1):
		line = fp_r.readline()
		if line=="":
			break
		if int(line.split(',')[-1])>0:
			nonzeros += 1.0
		else:
			zeros += 1.0
		if ("test" in filename):
			fp_w.write(line.strip()+",1.0\n")
	fp_r.close()
	if ("test" in filename):
		fp_w.close()
		continue
	if ((zeros == 0.0) or (zeros<nonzeros)):
		factor = 1.0
	elif (nonzeros == 0.0):
		factor = 1.0
		del_list.append(os.path.join(output_dir,filename))
	else:
		factor = (float(zeros)/nonzeros)
	fp_r = open(os.path.join(input_dir,filename))
	for i in xrange(7+T):
		fp_r.readline()
	while(1):
		line = fp_r.readline()
		if line=="":
			break
		if int(line.split(',')[-1])>0:
			fp_w.write(line.strip()+","+str(factor)+"\n")
		else:
			fp_w.write(line.strip()+","+str(1.0)+"\n")
	fp_w.close()		
	#~ else:
		#~ fp_r = open(os.path.join(input_dir,filename))
		#~ fp_w = open(os.path.join(output_dir,filename),"w")
		#~ fp_w.write(fp_r.read())
		#~ fp_w.close()
		#~ fp_r.close()

print "Deleting files..."
for i in del_list:
	print i
	os.system("rm "+i)
	print i.replace("train","test").replace("test","train",1)
	os.system("rm "+i.replace("train","test").replace("test","train",1))
