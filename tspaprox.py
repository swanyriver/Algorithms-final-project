import getcities

import sys

if len(sys.argv) < 2: 
  print "must supply input file"
  exit()


cities = getcities.readCities(sys.argv[1])

for line in cities:
  print line