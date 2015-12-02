import getcities
import primm

import sys

if len(sys.argv) < 2: 
  print "must supply input file"
  exit()


cities = getcities.readCities(sys.argv[1])

for line in cities[:10]:
  print line

cities = getcities.readCities(sys.argv[1], primm.primcity)

for line in cities[:10]:
  print line
