import os
input_dir = "gridfiles/"
output_dir = "output_months_csv/"
files = os.listdir(input_dir)

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

day_list = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
for weekdays_no in xrange(7):
	CLASS_day = day_list[weekdays_no]
	new_output_dir = os.path.join(output_dir,CLASS_day)
	try:
		os.mkdir(os.path.join(output_dir,CLASS_day))
	except:
		pass
	for filename in files:
		if (os.stat(os.path.join(input_dir,filename)).st_size!=0L):
			fp_r = open(os.path.join(input_dir,filename))
			print "Opening ", os.path.join(input_dir,filename)
			fp_w = open(os.path.join(new_output_dir,filename.split('.')[0]+'.csv') , 'w')
			##
			month_count = []
			for i in xrange(117):		# 117 is the total number of months from Jan '03 to Sep '12
				month_count.append(0)
			for line in fp_r:
				if (line.split(',')[3]==CLASS_day):
					##
					tally = 0
					month = int(line.split(',')[4])
					year = int(line.split(',')[6])
					tally += (year-2003)*12
					tally += month-1
					month_count[tally]+=1
					##
			fp_w.write("day,month,count\n")
			for i in xrange(117):
				fp_w.write(str(weekdays_no)+",")
				fp_w.write(str(i+1)+","+str(month_count[i])+"\n")
			##
			fp_w.close()
			fp_r.close()
