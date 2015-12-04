import getcities
import nearestneighbor
from math import sqrt
import sys
from itertools import izip_longest

def distance(u,v):
  return int(round(sqrt( (u.x-v.x)**2 + (u.y-v.y)**2 )))

def tourdistance(tour):
  return sum( distance(tour[u],tour[v]) 
    for u,v in 
    izip_longest(range(len(tour)),range(1,len(tour)), fillvalue=0) )

def setindex(city,i):
  city.index = i
  return city

def updateindexes(tour,start,end):
  tour[start:end] = [setindex(tour[i],i) for i in range(start,end)]

def swap(tour,b,c):
  #print "swaping city%d @%d and city%d @%d"%(b.id,b.index,c.id,c.index)
  tour[b.index:c.index+1] = reversed(tour[b.index:c.index+1])
  updateindexes(tour,b.index,c.index+1)


def unsqrtdistance(u,v):
  return (u.x-v.x)**2 + (u.y-v.y)**2 


def twoopt(tour):
  updateindexes(tour,0,len(tour))

  for a in list(tour):

    for c in [x.city for x in a.neighbors]:

      if a.index>c.index: a,c = c,a

      b = tour[a.index+1]
      d = tour[(c.index+1)%len(cities)]

      if b is not c and distance(a,b) + distance(c,d) > distance(a,c) + distance(b,d):
        swap(tour,b,c)


if len(sys.argv) < 2: 
  print "must supply input file"
  exit()


cities = getcities.readCities(sys.argv[1], nearestneighbor.nearcity)

nearestneighbor.nearneighbortour(cities)

totaldistance = tourdistance(cities)
improvment = 1
while improvment:
  print totaldistance
  twoopt(cities)
  newdistance = tourdistance(cities)
  improvment = totaldistance - newdistance
  totaldistance = newdistance

#twoopt(cities)

print tourdistance(cities)

# print "\n".join([str(x.id) + str([y.city.id for y in x.neighbors[:-1]]) for x in cities])
#print "\n".join([str(x.id) for x in cities])



