import getcities
import nearestneighbor
from math import sqrt

import sys

def distance(u,v):
    return int(round(sqrt( (u.x-v.x)**2 + (u.y-v.y)**2 )))

if len(sys.argv) < 2: 
  print "must supply input file"
  exit()


cities = getcities.readCities(sys.argv[1], nearestneighbor.nearcity)

nearestneighbor.nearneighbortour(cities)

from itertools import izip_longest
print sum( distance(cities[u],cities[v]) 
    for u,v in 
    izip_longest(range(len(cities)),range(1,len(cities)), fillvalue=0) )

# print "\n".join([str(x.id) + str([y.city.id for y in x.neighbors[:-1]]) for x in cities])
#print "\n".join([str(x.id) for x in cities])



