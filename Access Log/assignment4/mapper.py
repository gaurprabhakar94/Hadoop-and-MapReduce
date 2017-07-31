#!/usr/bin/python


import sys

for line in sys.stdin:
    data = line.replace('[','').replace(']','').replace('"','').split(' ')
    if len(data) == 10:
        (IP, ID, uname, date_time, zone, method, path, qstr_pro_req, status, size) = data
        print "{0}".format(path)

