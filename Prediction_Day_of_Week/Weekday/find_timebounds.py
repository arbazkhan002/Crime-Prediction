min = 222222
max = 0
min_month = 24
max_month = -23
f = open('new_data.csv')
for line in f:
	year = int(line.split(',')[6])
	month = int(line.split(',')[4])
	if year<min:
		min = year
		minmonth = 24
	if year>max:
		max = year
		maxmonth = -23
	if (year == min):
		if (month<minmonth):
			minmonth = month
	if (year == max):
		if (month>maxmonth):
			maxmonth = month
print "min year =", min, "min month =", minmonth
print "max year =", max, "max month =", maxmonth
