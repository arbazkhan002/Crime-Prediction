import os
import sys
for i in xrange(60,80):
	try:
		os.system("java AddWeightsFromAtt alldays_weighted_median_5/"+str(i)+"test.arff 9 xrff_median_7/gen_"+str(i)+"test.xrff")
	except:
		pass
	try:
		os.system("java AddWeightsFromAtt alldays_weighted_median_5/"+str(i)+"train.arff 9 xrff_median_7/gen_"+str(i)+"train.xrff")
	except:
		pass
