import random
random.seed()

class Neighbor(object):
  """docstring for neighbor"""
  def __init__(self, city, distance):
    self.city = city
    self.distance = distance
  def __eq__(self,other): 
    return self.distance == other.distance
  def __lt__(self,other): 
    return self.distance < other.distance
  def __le__(self,other): 
    return self.distance <= other.distance
  def __gt__(self,other): 
    return self.distance > other.distance
  def __ge__(self,other): 
    return self.distance >= other.distance
    

class nearcity(object):
  """subclass of tsp city for nearest neighbor"""
  def __init__(self, num, x,y, NUMNEIGHBORS = 20):
    self.id = num
    self.x = x
    self.y = y
    self.neighbors = []
    self.NUMNEIGHBORS = NUMNEIGHBORS

  def addneighbor(self,city, distance):
    self.neighbors.append( Neighbor(city,distance) )

    if len(self.neighbors) == self.NUMNEIGHBORS:
      self.neighbors.sort()
      self.neighbors.append(None)
      self.addneighbor = self.capacityaddneighbor

  def capacityaddneighbor(self,city, distance):

    if distance >= self.neighbors[-2].distance:return

    self.neighbors[-1] = Neighbor(city, distance)
    self.neighbors.sort()



def setindex(city,i):
  city.index = i
  return city

def updateindexes(tour,start,end):
  tour[start:end] = [setindex(tour[i],i) for i in range(start,end)]


def nearneighbortour(cities,rindex = None):

  updateindexes(cities,0,len(cities))

  if rindex == None: rindex=random.randrange(len(cities))

  cities[rindex],cities[0] = cities[0],cities[rindex]
  cities[rindex].index,cities[0].index = rindex,0

  for u in range(0,len(cities)-1):

    usableNeighbors = [x.city for x in cities[u].neighbors if x.city.index > u]

    if usableNeighbors:
      cities[u+1], cities[usableNeighbors[0].index] = cities[usableNeighbors[0].index], cities[u+1]
      cities[u+1].index = u+1
      cities[usableNeighbors[0].index].index = usableNeighbors[0].index
      continue

    nearNBIndex = None
    nearNBDist = float('inf')  
    for v in range(u+1,len(cities)):

      distance = (cities[u].x - cities[v].x)**2 + (cities[u].y - cities[v].y)**2
      if distance < nearNBDist:
        nearNBDist = distance
        nearNBIndex = v

    cities[u+1],cities[nearNBIndex] = cities[nearNBIndex],cities[u+1]
    cities[u+1].index = u+1
    cities[nearNBIndex].index = nearNBIndex



def nearneighbors(cities):

  for u,v in ((u,v) for u in range(len(cities)) for v in range(len(cities)) if u != v):
    cities[u].addneighbor(cities[v], (cities[u].x - cities[v].x)**2 + (cities[u].y - cities[v].y)**2 )








