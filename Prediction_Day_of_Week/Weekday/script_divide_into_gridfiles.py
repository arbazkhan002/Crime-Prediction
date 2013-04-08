import time
import os
def clear_all(count):
	for i in xrange(count):
		print "Removing "+str(i)
		os.system("rm gridfiles"+str(i)+"/*")
		os.system("rmdir gridfiles"+str(i))
		os.system("rm new_data"+str(i)+".csv")

def foo(arg):
	f = open("new_data"+str(arg)+".csv",'r')
	siz = 0
	strings = []
	for i in xrange(900):
		strings.append("")
	outside_city = ""
	count = 0
	for line in f:
		count += 1
		gridno = int(line.split(',')[-1])
		if (gridno==732732):
			outside_city = outside_city+line
		else:
			strings[gridno] = strings[gridno]+line
	try:
		os.mkdir("gridfiles"+str(arg))
	except OSError:
		pass
	for i in xrange(900):
		newfile = open("gridfiles"+str(arg)+"/"+str(i)+".csv",'w')
		newfile.write(strings[i])
		newfile.close()
	newfile = open("gridfiles"+str(arg)+"/"+str(732732)+".csv",'w')
	newfile.write(outside_city)
	newfile.close()
	f.close()

def do_concatenate(count2):
	print "Concatenating..."
	try:
		os.mkdir("gridfiles")
	except OSError:
		pass
	for i in xrange(900):
		fp_to_write = open("gridfiles/"+str(i)+".csv",'w')
		for j in xrange(count2):
			reading = open("gridfiles"+str(j)+"/"+str(i)+".csv").read()
			fp_to_write.write(reading)
		fp_to_write.close()
		print "Final file made:"+str(i)
	fp_to_write = open("gridfiles/"+str(732732)+".csv",'w')
	for j in xrange(count2):
		reading = open("gridfiles"+str(j)+"/"+str(732732)+".csv").read()
		fp_to_write.write(reading)
	fp_to_write.close()
	print "Final file made:"+str(732732)

def main():
	#~ fp = open("new_data.csv",'r')
	fp = open("sample_newdata.csv",'r')
	count = 0
	count2 = 0
	data = ""
	for line in fp:
		count+= 1
		data += line
		if ((count%100000)==0):
			fp = open("new_data"+str(count2)+".csv",'w')
			fp.write(data)
			fp.close()
			count2+= 1
			data = ""
	fp = open("new_data"+str(count2)+".csv",'w')
	fp.write(data)
	fp.close()
	count2+= 1
	data = ""
	for i in xrange(count2):
		print "calling foo("+str(i)+")"
		time.sleep(1)
		foo(i)
	do_concatenate(count2)
	clear_all(count2)

if __name__ == "__main__":
	main()
