import getcities
import nearestneighbor
from math import sqrt
import sys

def setindex(city,i):
  city.index = i
  return city

def updateindexes(tour,start,end):
  tour[start:end] = [setindex(tour[i],i) for i in range(start,end)]


def unsqrtdistance(u,v):
  return (u.x-v.x)**2 + (u.y-v.y)**2 

def twoopt(tour):
  updateindexes(tour,0,len(tour))

  index = 0
  while index < len(tour):

    trade = min(tour[index].neighbors)

    #ahhhhhh, what if it is going the other way,  what if it crosses over the seam :(

    bindex = tour[index].city.index+1%len(cities)
    dindex = trade.city.index+1%len(cities)

    if trade.distance < unsqrtdistance(tour[],tour[]):
      trade


    index += 1


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

twoopt(cities)

# print "\n".join([str(x.id) + str([y.city.id for y in x.neighbors[:-1]]) for x in cities])
#print "\n".join([str(x.id) for x in cities])



