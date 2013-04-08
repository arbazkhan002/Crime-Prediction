#~ IncidntNum,Category,Descript,DayOfWeek,Month,Day,Year,Hours,Minute,PdDistrict,Resolution,bin
#~ Crime count in past 3 months
# import time
import pickle
f=open("final_data.csv")


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
		return map(get_grid_value, [g-1,g+29,g+30,g-31,g-30])
	else:
		return map(get_grid_value, [g+1,g-1,g+29,g+30,g+31,g-29,g-30,g-31])
	
def average_crime(neighbors,date):
	sums = 0
	for neighbor in neighbors:
		try:
			sums+=neighbor[date][0]
		except:
			sums+=0
	return float(sums)/len(neighbors)

time_arr=[{} for i in range(900)]
#~ [ [ {} {} {} , ...... ] , [ {} {} {} , ... ] , ....... ]
	
monther1=[31,28,31,30,31,30,31,31,30,31,30,31]
monther2=[31,29,31,30,31,30,31,31,30,31,30,31]

yearl = [2004,2008,2012]
t=9

for line in f:
	l=line.split(",")
	# hour=int(l[7]) 
	grid = int(l[-1])
	if grid==732732:
		continue
	
	day_dict=time_arr[grid]
	#~ 
	month,day,year=map(int,l[4:7])
	dayno=year*100+month
	if dayno not in day_dict:
		day_dict[dayno]=[0,0,0,0,0,0,0,0,0,0,0]
	day_dict[dayno][10]+=1
	
	
	for i in range(1,10):		
		dayd=dayno
		if year in yearl:
			monther = monther2
		else:
			monther = monther1	
		if month+i>12:
			dayd=(year+1)*100+(month+i)%12
		else:
			dayd+=i
			
		# if (dayd+i)%100>monther[month-1]:
			# if month==12:
				# dayd=(year+1)*10000+100+(i+day)%31
			# else:								
				# if month==1 and day in [30,31]:
					# if (day+i)-31>monther[1]:
						# dayd+=200+i-31-monther[1]				
				# else:
					# dayd+=100 + i%monther[(month)%12]-day
					
				
		# else:
			# dayd+=i
		
		if dayd%100>12:			
			print dayd, line 
		
		
		if dayd not in day_dict:
			day_dict[dayd]=[0,0,0,0,0,0,0,0,0,0,0]		
		day_dict[dayd][0]+=1
		day_dict[dayd][i]+=1

#~ tp="grid_pickle/"
#~ for i in range(len(time_arr)):
	#~ f=open(tp+str(i)+".p","w")
	#~ pickle.dump(time_arr[i],f)
	#~ f.close()

f.close()
f = open("monthly_train_not_hourly_t9.csv","w")
#~ g = open("final_data.csv")

for i in time_arr:
	# for j in i:
	for k in i:
		grid = time_arr.index(i)
		# hour = i.index(j)
		# print get_neighbors(grid)
		# time.sleep(0.1)
		# if dayd%100 ==1:
			# print 'hello hello'
		f.write(str(grid)+","+str(k)+","+str(i[k][0])+","+str(i[k][1])+","+str(i[k][2])+","+str(i[k][3])+","+str(i[k][4])+","+str(i[k][5])+","+str(i[k][6])+","+str(i[k][7])+","+str(i[k][8])+","+str(i[k][9])+","+str(average_crime(get_neighbors(grid),k))+","+str(i[k][10])+"\n")
		# format of the csv file is grid_no, hour, year_month, TCC_prev_3_months, TCC 1 month back, TCC 2 month back, TCC 3 month back, TCC average neighbourhood prev 3 months, TCC this month
f.close()