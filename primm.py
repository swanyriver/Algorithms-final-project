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
  #cities[rindex] = cities[0]
  #cities[0] = r

  r.key = 0

  for i in range(len(cities)-1,-1,-1):
    
    #heap pop and city removed from Q
    uindex = min(xrange(len(cities[:i+1])),key=cities.__getitem__)
    u = cities[uindex]

    #u = cities[0]
    #cities[0] = cities[i]
    cities[uindex] = cities[i]
    cities[i] = u

    for v in cities[:i]:
      #non sqrt distances are compared
      #v.key = min((u.x-v.x)**2 + (u.y-v.y)**2,v.key)
      newkey = (u.x-v.x)**2 + (u.y-v.y)**2
      if newkey < v.key:
        v.key = newkey
        v.predecessor = u


  #convert to a descendant tree
  for city in cities[:-1]:
    city.predecessor.descendants.append(city)


  return r


    

