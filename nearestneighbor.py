import functools

@functools.total_ordering
class Neighbor(object):
  """docstring for neighbor"""
  def __init__(self, city, distance):
    self.city = city
    self.distance = distance
    self.next = None
  def __eq__(self,other): 
    return self.distance == other.distance
    
  def __lt__(self,other): 
    return self.distance < other.distance

    

class nearcity(object):
  """subclass of tsp city for nearest neighbor"""
  NUMNEIGHBORS = 5
  def __init__(self, num, x,y):
    self.id = num
    self.x = x
    self.y = y
    self.neighbors = []
    self.neighborsback = self.neighborsfront
    self.INF = Neighbor(None,float('inf'))

  def addneighbor(city, distance):
    self.neighbors.append( Neighbor(city,distance) )

    if len(self.neighbors) == self.NUMNEIGHBORS:
      self.neighbors.sort()
      self.neighbors.append(self.INF)
      self.addneighbor = self.capacityaddneighbor

    return distance

  def capacityaddneighbor(city, distance):

    self.neighbors[-1] = Neighbor(city, distance)
    self.neighbors.sort()
    self.neighbors[-1] = self.INF

    return distance



  # def __repr__(self):
  #   return "pcity id:%d x:%d y:%d  predecessor:%r, descendants:%r"%(self.id,self.x,self.y, self.predecessor.id if self.predecessor else None, [x.id for x in self.descendants] )

  # def __str__(self):
  #   return self.__repr__()

import random
random.seed()

def nearneighbortour(cities,rindex = None):

  if rindex == None: rindex=random.randrange(len(cities))

  cities[rindex],cities[0] = cities[0],cities[rindex]

  for u in range(0,len(cities)):
    for v in range(0,u):
      cities[u].addneighbor(cities[v], (cities[u].x - cities[v].x)**2 + (cities[u].y - cities[v].y)**2 )

    nearNBIndex = u
    nearNBDist = float('inf')  
    for v in range(u+1,len(cities)):

      distance = (cities[u].x - cities[v].x)**2 + (cities[u].y - cities[v].y)**2
      cities[u].addneighbor(cities[v], distance)
      if distance < nearNBDist:
        nearNBDist = distance
        nearNBIndex = v

    cities[u+1],cities[nearNBIndex] = cities[nearNBIndex],cities[u+1]







