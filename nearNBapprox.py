import getcities
import nearestneighbor
from math import sqrt
import sys
from itertools import izip_longest
from time import time

def distance(u,v):
  return int(round(sqrt( (u.x-v.x)**2 + (u.y-v.y)**2 )))

def tourdistance(tour):
  return sum( distance(tour[u],tour[v]) 
    for u,v in 
    izip_longest(range(len(tour)),range(1,len(tour)), fillvalue=0) )

def swap(tour,b,c):
  #print "swaping city%d @%d and city%d @%d"%(b.id,b.index,c.id,c.index)
  tour[b.index:c.index+1] = reversed(tour[b.index:c.index+1])
  nearestneighbor.updateindexes(tour,b.index,c.index+1)


def unsqrtdistance(u,v):
  return (u.x-v.x)**2 + (u.y-v.y)**2 


def twoopt(tour):

  swapcount = 0

  nearestneighbor.updateindexes(tour,0,len(tour))

  for a in list(tour):

    for c in [x.city for x in a.neighbors[:-1]]:

      if a.index>c.index: a,c = c,a

      b = tour[a.index+1]
      d = tour[(c.index+1)%len(cities)]

      if b is not c and distance(a,b) + distance(c,d) > distance(a,c) + distance(b,d):
        swap(tour,b,c)
        swapcount +=1

  return swapcount


########################################
##########MAIN##########################
########################################

STARTTIME = time()
MAXTIME = float('inf') if len(sys.argv) < 3 else int(sys.argv[2]) 

if len(sys.argv) < 2: 
  print "must supply input file"
  exit()



cities = getcities.readCities(sys.argv[1], nearestneighbor.nearcity)
nearestneighbor.nearneighbors(cities)

#assert [x.index for x in cities] == range(len(cities))
#assert sorted(x.id for x in cities) == range(len(cities))


besttour = float('inf')
besttourstring = ""

hardcopycities = cities
#from random import shuffle
#shuffle(hardcopycities)

twoopts = []

i = 0
#for i in range(len(cities)):
#for i in range(1):
while ( i < len(cities) and time() - STARTTIME < MAXTIME ) or i == 0:

  #print cities[i].id, time() - STARTTIME, MAXTIME

  twooptcount = 0

  cities = list(hardcopycities)

  #print i, " getting tour"
  nearestneighbor.nearneighbortour(cities,i)

  totaldistance = tourdistance(cities)
  #print " (root:%d) tour gotten distance: "%cities[0].id, totaldistance
  improvment = 1
  while improvment:
    twooptcount += twoopt(cities)
    newdistance = tourdistance(cities)
    improvment = totaldistance - newdistance
    totaldistance = newdistance

    if time() - STARTTIME >= MAXTIME: break

  #print " two opt finished: ", totaldistance

  twoopts.append(twooptcount)

  if totaldistance < besttour:
    besttour = totaldistance
    besttourstring = "\n".join([str(x.id) for x in cities])

  i+=1


print "Optimization complete with a total path distance of:", besttour
print "%d tours constructed with Nearest Neighbor Hueristic and improved with an average of %d 2-opt swaps"%(i,sum(twoopts)/len(twoopts))

f = open(sys.argv[1] + ".tour", "w")
f.write("%d\n%s"%(besttour,besttourstring))
f.close()
#print besttourstring