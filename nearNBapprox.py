import getcities
import nearestneighbor
from math import sqrt
import sys
from itertools import izip_longest
from time import time

#caclulate rounded distance between u and v
def distance(u,v):
  return int(round(sqrt( (u.x-v.x)**2 + (u.y-v.y)**2 )))

#calculate total distance of a tour
def tourdistance(tour):
  #izip_longest returns a generator with tupples [(0,1),(1,2) .. (n-1,n),(n,0)]
  return sum( distance(tour[u],tour[v]) 
    for u,v in 
    izip_longest(range(len(tour)),range(1,len(tour)), fillvalue=0) )

#perform a 2-opt swap by reversing vertexes between
def swap(tour,b,c):
  tour[b.index:c.index+1] = reversed(tour[b.index:c.index+1])
  nearestneighbor.updateindexes(tour,b.index,c.index+1)

def twoopt(tour):

  nearestneighbor.updateindexes(tour,0,len(tour))

  for a in list(tour):

    for c in [x.city for x in a.neighbors[:-1]]:

      if a.index>c.index: a,c = c,a

      #b = vertex adjacent to a and between a and c
      b = tour[a.index+1]

      #d = vertex adjacent to c and not between a and c
      d = tour[(c.index+1)%len(cities)]

      #removing edges a,b and c,d will result in creating edges a,c and b,d
      #                                        and reversing vertexes b---c
      #only do so if the distance of the edges removed is greater then the ones created
      if b is not c and distance(a,b) + distance(c,d) > distance(a,c) + distance(b,d):
        swap(tour,b,c)


########################################
##########MAIN##########################
########################################

#measure begingin time and set maximum time
STARTTIME = time()
if len(sys.argv) < 3: MAXTIME = float('inf')
else: MAXTIME = STARTTIME + int(sys.argv[2])

#ensure file to read is supplied
if len(sys.argv) < 2: 
  print "must supply input file"
  exit()

#read cities from file
cities = getcities.readCities(sys.argv[1], nearestneighbor.nearcity)

#create list of nearest neighbors for each city
nearestneighbor.nearneighbors(cities)

besttour = float('inf')
besttourstring = ""

hardcopycities = cities

i = 0
while ( i < len(cities) and time() < MAXTIME ) or i == 0:

  cities = list(hardcopycities)

  nearestneighbor.nearneighbortour(cities,i)

  totaldistance = tourdistance(cities)
  improvment = 1
  while improvment:
    twoopt(cities)
    newdistance = tourdistance(cities)
    improvment = totaldistance - newdistance
    totaldistance = newdistance

    if time() >= MAXTIME: break

  if totaldistance < besttour:
    besttour = totaldistance
    besttourstring = "\n".join([str(x.id) for x in cities])

  i+=1

#output best found tour to file
f = open(sys.argv[1] + ".tour", "w")
f.write("%d\n%s"%(besttour,besttourstring))
f.close()
