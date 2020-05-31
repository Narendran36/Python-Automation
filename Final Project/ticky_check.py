#!/usr/bin/env python3

import re
import csv
import operator

e_d = {}
u_d = {}

with open("syslog.log") as lf:

 for line in lf.readlines():
  line = line.strip()
  info = re.search(r"ticky: INFO ([\w ']*) \[.*\] \((.*)\)", line)
  error = re.search(r"ticky: ERROR ([\w ']*) \((.*)\)", line)

  if error is not None:
   if error[1] not in e_d:
    e_d[error[1]] = 1
   else:
    e_d[error[1]] += 1

   if error[2] not in u_d:
    u_d[error[2]] = [0,1]
   else:
    u_d[error[2]][1] += 1


  if info is not None:  
   if info[2] not in u_d:
    u_d[info[2]] = [1,0]
   else:
    u_d[info[2]][0] += 1

 e_d = sorted(e_d.items(), key=operator.itemgetter(1), reverse=True)
 u_d = sorted(u_d.items(), key=operator.itemgetter(0))[0:8] #remove [0:8] to choose all rows, instead of first eight rows 


 e_header = ["Error","Count"]
 u_header = ["Username","INFO","ERROR"]

with open("error_message.csv", "w", newline='') as ef:
 writer = csv.DictWriter(ef, fieldnames=e_header)
 writer.writeheader()
 for key,value in e_d:
  writer.writerow({"Error": key, "Count": value})

with open("user_statistics.csv", "w", newline='') as uf:
 writer = csv.DictWriter(uf, fieldnames=u_header)
 writer.writeheader() 
 for key,value in u_d:
  writer.writerow({"Username": key, "INFO": value[0], "ERROR": value[1]})
