import random
random.seed()

#object for tracking each cities nearest neighbors
#a distance to the city holding the object, and pointer to city object
#total ordering functions defined so that comparisons and sorting can be done nativly
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
    
#city object for use in nearest neighbor hueristic
#maintains a list of nearest other citys
class nearcity(object):
  """subclass of tsp city for nearest neighbor"""
  def __init__(self, num, x,y, NUMNEIGHBORS = 10):
    self.id = num
    self.x = x
    self.y = y
    self.neighbors = []
    self.NUMNEIGHBORS = NUMNEIGHBORS

  #add a new neighbor indiscriminatley before capacity is reached
  def addneighbor(self,city, distance):
    self.neighbors.append( Neighbor(city,distance) )

    #change method to one that will perseve sorted order of neighbors
    if len(self.neighbors) == self.NUMNEIGHBORS:
      self.neighbors.sort()
      self.neighbors.append(None)
      self.addneighbor = self.capacityaddneighbor

  def capacityaddneighbor(self,city, distance):

    #this city is farter away than any of the cities in my list
    if distance >= self.neighbors[-2].distance:return

    #the list stays the same size always, 1 more than limit
    #item is added to end and the list is sorted
    #with such a small list and the native timsort being optimized for somewhat sorted lists
    #this is at or near the optimizations that could be achieved with a linked list or avl tree
    self.neighbors[-1] = Neighbor(city, distance)
    self.neighbors.sort()


#used by update index
def setindex(city,i):
  city.index = i
  return city

#sets index field of a section of the tour to match their actual position
def updateindexes(tour,start,end):
  tour[start:end] = [setindex(tour[i],i) for i in range(start,end)]


#create a new tour of the cities using Nearest Neighbor Hueristic
def nearneighbortour(cities,rindex = None):

  updateindexes(cities,0,len(cities))

  if rindex == None: rindex=random.randrange(len(cities))

  #start by moving provided or randomly chosen root to begin of list
  cities[rindex],cities[0] = cities[0],cities[rindex]
  cities[rindex].index,cities[0].index = rindex,0

  #loop invariant:  at begining of loop cities[0 through and including u] are in tour order
  for u in range(0,len(cities)-1):

    #filter neighbors that are already in tour
    usableNeighbors = [x.city for x in cities[u].neighbors if x.city.index > u]

    #next city in tour is u's nearest neighbor not in tour
    if usableNeighbors:
      cities[u+1], cities[usableNeighbors[0].index] = cities[usableNeighbors[0].index], cities[u+1]
      cities[u+1].index = u+1
      cities[usableNeighbors[0].index].index = usableNeighbors[0].index
      continue

    #must search beyond the already recorded near neighbors
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


#populates a nearest M neighbors list for every vertex
def nearneighbors(cities):

  #itterate over all permutations (u,v) excluding u==v
  for u,v in ((u,v) for u in range(len(cities)) for v in range(len(cities)) if u != v):
    #add v to us neighbors list if its distance is less than any already in list
    cities[u].addneighbor(cities[v], (cities[u].x - cities[v].x)**2 + (cities[u].y - cities[v].y)**2 )








