import sys
import os
input_dir = "output_months_csv/"
#~ input_dir = "dummy/"
output_dir = "nominal_training_data/"

def find_median(array):
	copyarray = [i for i in array]
	copyarray.sort()
	if (len(copyarray)%2==0):
		return (float(copyarray[int(len(copyarray)/2)])+float(copyarray[int(len(copyarray)/2-1)]))/2.0
	else:
		return copyarray[int(len(copyarray)/2)]

def find_mean(array):
	return float(sum(array))/len(array)

def find_std(array,mean):
	ans = 0.0
	for dataval in array:
		ans += pow(dataval-mean,2)
	ans = pow( ans/len(array) , 0.5 )
	return ans

def get_neighbors(g):
	if g in [0,29,899,870]:
		if g==0:
			return [1,30,31]
		elif g==29:
			return [28,58,59]
		elif g==899:
			return [898,868,869]
		elif g==870:
			return [871,870,841]
	elif g<30:
		return [g+1,g-1,g+29,g+30,g+31]
	elif g>870:
		return [g+1,g-1,g-29,g-30,g-31]
	elif g%30==0:
		return [g+1,g-30,g+30,g+31,g-29]
	elif (g+1)%30==0:
		return [g-1,g+29,g+30,g-31,g-30]
	else:
		return [g+1,g-1,g+29,g+30,g+31,g-29,g-30,g-31]

if len(sys.argv)==2:
	T = int(sys.argv[1])		# T-month approach
else:
	print "sys.argv is not 2."
	exit(1)

day_list = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
for weekdays_no in xrange(7):
	CLASS_day = day_list[weekdays_no]
	new_output_dir = os.path.join(output_dir,CLASS_day)
	new_input_dir =os.path.join(input_dir,CLASS_day)
	try:
		os.mkdir(new_output_dir)
	except:
		pass
	files = os.listdir(new_input_dir)
	os.system("rm "+os.path.join(new_output_dir,"*"))		# Clearing the output directory first
	for filename in files:
		fp_r = open(os.path.join(new_input_dir,filename))
		print "Opening ", os.path.join(input_dir,filename)
		fp_w = open(os.path.join(new_output_dir,filename.split('.')[0]+'train.csv') , 'w')
		##
		blockno = int(filename.split('.')[0])
		training_file = []
		nbr_list = get_neighbors(blockno)
		nbr_fp_list = []
		for i in nbr_list:
			print "\tNeighbour:", i, 
			try:
				fp = open(os.path.join(new_input_dir,str(i)+'.csv'))
				print 'opened'
			except:
				print 'not opened'
				continue
			fp.readline()
			array = []
			for i in xrange(117):
				array.append(int(fp.readline().split(',')[-1]))
			nbr_fp_list.append(array)
		fp_r.readline()
		array = []
		for i in xrange(117):
			array.append(int(fp_r.readline().split(',')[-1]))
		# array = This block entries
		# nbr_fp_list = Neighbour's entries

		#~ mean = find_mean(array)
		mean = find_median(array)
		#~ stddev = find_std(array,mean)
		modified_array = []

		for dataval in array:
			if (dataval>0):
				modified_array.append(1)
			else:
				modified_array.append(0)

		#~ for dataval in array:
			#~ if (dataval <= mean):
				#~ modified_array.append(0)	#low risk
			#~ else:
				#~ modified_array.append(1)	#high risk

		#~ for dataval in array:
			#~ if (dataval < mean-stddev):
				#~ modified_array.append(0)	#low risk
			#~ elif (dataval > mean+stddev):
				#~ modified_array.append(2)	#high risk
			#~ else:
				#~ modified_array.append(1)	#medium risk

		fp_w.write("day,")
		for i in xrange(T,0,-1):
			fp_w.write("month"+str(i)+",")
		fp_w.write("nbr_total"+str(T)+",this_month\n")

		for i in xrange(117-T):
			nbr_count = 0
			fp_w.write(str(weekdays_no)+",")
			for j in xrange(T):
				for sldf in nbr_fp_list:
					nbr_count += sldf[i+j]
				fp_w.write(str(array[i+j])+",")
			fp_w.write(str(nbr_count)+",")
			fp_w.write(str(modified_array[i+T])+"\n")
		##
		fp_w.close()
		fp_r.close()
