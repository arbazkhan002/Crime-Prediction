#~ Template code file for the data generator. Other files with the prefix 'gridbased' are variants of this file.
import pickle

def get_grid_value(g):
	return time_arr[g]

def get_neighbors(g):
	if g in [0,29,899,870]:
		if g==0:
			return map(get_grid_value, [1,30,31])
		elif g==29:
			return map(get_grid_value, [28,58,59])
		elif g==899:
			return map(get_grid_value, [898,868,869])
		elif g==870:
			return map(get_grid_value, [871,870,841])
	elif g<30:
		return map(get_grid_value, [g+1,g-1,g+29,g+30,g+31])
	elif g>870:
		return map(get_grid_value, [g+1,g-1,g-29,g-30,g-31])
	elif g%30==0:
		return map(get_grid_value, [g+1,g-30,g+30,g+31,g-29])
	elif (g+1)%30==0:
		return map(get_grid_value, [g-1,g+29,g+30,g+31,g-30])
	else:
		return map(get_grid_value, [g+1,g-1,g+29,g+30,g+31,g-29,g-30,g-31])
	
def average_crime(neighbors,hour,date):
	sums = 0
	for neighbor in neighbors:
		try:
			sums+=time_arr[neighbor][hour][date][0]
		except:
			sums+=0
	return sums/len(neighbors)


f = open("time_arr.p")
time_arr = pickle.load(f)
f.close()

f = open("train.csv","w")
#~ g = open("final_data.csv")

for i in time_arr[:1]:
	for j in i[:1]:
		for k in j:
			grid = time_arr.index(i)
			hour = i.index(j)
			f.write(str(grid)+","+str(hour)+","+str(k)+","+str(j[k][0])+","+str(average_crime(get_neighbors(grid),hour,k))+","+str(j[k][1]))
			
f.close()
