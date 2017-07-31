#!/usr/bin/python

import sys
count = 0
path = None
highPath = None
highCount = 0

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
	data_mapped = line.strip()
	
	
	
	if path and path == data_mapped:  		
		count += 1
	
	else:
		if highCount < count:
			highCount = count			
			highPath = path
					
		path = data_mapped
		count = 1

if path !=None:
	print highPath, '\t', highCount
