import sys
import os
input_dir = "nominal_training_data/"
output_dir = "nominal_training_data/alldays/"
try:
	os.mkdir(output_dir)
except:
	pass
files = os.listdir(os.path.join(input_dir, "Monday"))

if len(sys.argv)==2:
	T = int(sys.argv[1])		# T-month approach	#117-T entries in each file
else:
	print "sys.argv is not 2."
	exit(1)

K = 16	# No of lines to put in test

day_list = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
for filename in files:
	print "--Starting merging for", filename
	fp_w = open(os.path.join(output_dir,filename.replace("csv","arff")),'w')
	fp_w2 = open(os.path.join(output_dir,filename.replace('train','test').replace("csv","arff")),'w')
	for weekdays_no in xrange(7):
		CLASS_day = day_list[weekdays_no]
		new_input_dir = os.path.join(input_dir,CLASS_day)
		fp_r = open(os.path.join(new_input_dir,filename))
		if (weekdays_no==0):
			papad = fp_r.readline()
			papad = "@relation xyz_test_train\n\n@attribute day {0,1,2,3,4,5,6}\n"
			for i in range(T,0,-1):
				papad += "@attribute month"+str(i)+" numeric\n"
			papad += "@attribute prev_"+str(T)+"_sum numeric\n@attribute class {0,1}\n\n@data\n"
			fp_w.write(papad)
			fp_w2.write(papad)
		else:
			fp_r.readline()
		for jj in xrange(117-T-K):
			fp_w.write(fp_r.readline())
		for jj in xrange(K):
			fp_w2.write(fp_r.readline())
		fp_r.close()
	fp_w.close()
	fp_w2.close()
