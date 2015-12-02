import heapq
import functools
import random
random.seed()

@functools.total_ordering
class primcity(object):
  """subclass of tsp city for primm"""
  def __init__(self, num, x,y):
    self.id = num
    self.x = x
    self.y = y
    self.key = float('inf')
    self.predecessor = None
    self.descendants = []

  def __eq__(self,other): 
    return self.key == other.key
    
  def __lt__(self,other): 
    return self.key < other.key

  def __repr__(self):
    return "pcity id:%d x:%d y:%d  predecessor:%r, descendants:%r"%(self.id,self.x,self.y, self.predecessor.id if self.predecessor else None, [x.id for x in self.descendants] )

  def __str__(self):
    return self.__repr__()


def primmtree(cities, rindex = None):

  if rindex == None: rindex=random.randrange(len(cities))

  r = cities[rindex]
  cities[rindex] = cities[-1]
  cities[-1] = r

  r.key = None
  u = r

  for i in range(len(cities)-2,0,-1):

    bestnextedge = float('inf')

    

    for v in range(i+1):
      #non sqrt distances are compared
      newkey = (u.x-cities[v].x)**2 + (u.y-cities[v].y)**2
      if newkey < cities[v].key:
        cities[v].key = newkey
        cities[v].predecessor = u
      if cities[v].key < bestnextedge:
        bestnextedge = newkey
        uindex = v

    u = cities[uindex]
    cities[uindex] = cities[i]
    cities[i] = u

  #convert to a descendant tree
  for city in cities[:-1]:
    city.predecessor.descendants.append(city)


  return r


    

