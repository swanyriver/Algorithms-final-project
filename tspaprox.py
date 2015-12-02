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

distances = []

for i in range(len(cities)):

    cities = getcities.readCities(sys.argv[1], primm.primcity)

    root = primm.primmtree(cities,i)

    stack = [root]
    tour = []

    while stack:
        city = stack.pop()
        tour.append(city)
        stack.extend(city.descendants)

    totaldistance = 0
    #this will not scale well
    for i,j in zip(range(len(tour)), range(1,len(tour)) + [0]):
        totaldistance += distance(tour[i],tour[j])
        #print i,":",tour[i].id

    print totaldistance
    distances.append(totaldistance)

print "minimum:",min(distances), " maximum:", max(distances)



# cities = getcities.readCities(sys.argv[1], primm.primcity)

# root = primm.primmtree(cities)

# stack = [root]
# tour = []

# while stack:
#     city = stack.pop()
#     tour.append(city)
#     stack.extend(city.descendants)

# totaldistance = 0
# #this will not scale well
# for i,j in zip(range(len(tour)), range(1,len(tour)) + [0]):
#     totaldistance += distance(tour[i],tour[j])
#     #print i,":",tour[i].id

# print totaldistance




