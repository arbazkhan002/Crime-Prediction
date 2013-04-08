import os
max_filename = ""
max_size = 0
for i in xrange(900):
	size = os.stat('gridfiles/'+str(i)+'.csv').st_size
	if size>max_size:
		max_size = size
		max_filename = 'gridfiles/'+str(i)+'.csv'
print "The maximum size is", max_size
print "The filename with maximum size is", max_filename
