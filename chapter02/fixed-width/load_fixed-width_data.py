#-*- coding: utf-8 -*-
#Edited by bighead 18-12-30

import struct
import string
import time

datafile = "ch02-fixed-width-1M.data"
mask = '9s15s5s'


time_start = time.time()
with open(datafile, 'r')as f:
    for line in f:
        #fields = struct.Struct(mask).unpack_from(line)
        fields = line.split(' ')
        #print 'fields: ', [field.strip() for field in fields]
        #print(fields)
time_end = time.time()
print time_end-time_start


time_start = time.time()
with open(datafile, 'r')as f:
    for line in f:
        fields = struct.Struct(mask).unpack_from(line)
time_end = time.time()
print time_end - time_start
