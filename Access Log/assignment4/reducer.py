#!/usr/bin/python

import sys
path = None
hitCount = 0

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
	data_mapped = line.strip()
	'''
	if len(data_mapped) != 1:
	        # Something has gone wrong. Skip this line.
	        continue
	'''
	if path and path == "/assets/js/the-associates.js":   		
		hitCount += 1
	path = data_mapped
	
print hitCount
