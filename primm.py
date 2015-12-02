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
    self.intree = False
    self.key = float('inf')
    self.predecessor = None

  def __eq__(self,other): 
    return self.key == other.key
    
  def __lt__(self,other): 
    return self.key < other.key

  def __repr__(self):
    return "pcity id:%d x:%d y:%d"%(self.id,self.x,self.y)

  def __str__(self):
    return self.__repr__()

    

def primmtree(cities):
  intree = [False] * len(cities)

  r = cities[random.randrange(len(cities))]

  r.key = 0

  Que = [r]
  intree[r.id]=True

  while  Que:
    u = heapq.heappop(Que)
    #for city in cities:

