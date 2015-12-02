import getcities
import primm

import sys

if len(sys.argv) < 2: 
  print "must supply input file"
  exit()



cities = getcities.readCities(sys.argv[1], primm.primcity)

root = primm.primmtree(cities)

for city in cities:
  print city


#for city in cities
