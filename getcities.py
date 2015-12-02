class City(object):
  """a cordinate point for TSP"""
  def __init__(self, num, x,y):
    self.id = num
    self.x = x
    self.y = y
  def __repr__(self):
    return "id:%d x:%d y:%d"%(self.id,self.x,self.y)
  def __str__(self):
    return self.__repr__()




def readCities(filename, cityconstructor=City):
  cityfile = open(filename,'r')

  cities = [ cityconstructor(*(int(x) for x in line.split(' ') if x)) for line in cityfile ]

  cityfile.close()

  return cities
    