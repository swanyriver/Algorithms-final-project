import getcities
import primm
from math import sqrt

import sys

def distance(u,v):
    return int(round(sqrt( (u.x-v.x)**2 + (u.y-v.y)**2 )))

if len(sys.argv) < 2: 
  print "must supply input file"
  exit()


cities = getcities.readCities(sys.argv[1], primm.primcity)

root = primm.primmtree(cities,5)

for city in cities:
  print city