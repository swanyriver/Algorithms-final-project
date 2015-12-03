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

distances = []


nearestneighbor.nearneighbortour(cities,13)

totaldistance = 0
#this will not scale well
for i,j in zip(range(len(cities)), range(1,len(cities)) + [0]):
    totaldistance += distance(cities[i],cities[j])
    #print i,":",cities[i].id

print totaldistance
# print "\n".join([str(x.id) + str([y.city.id for y in x.neighbors[:-1]]) for x in cities])
print "\n".join([str(x.id) for x in cities])



