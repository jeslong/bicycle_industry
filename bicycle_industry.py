class Bicycle(object):
  def __init__(self, model, cost, weight):
    self.model = model
    self.cost = cost
    self.weight = weight
    
class BikeShop(object):
  def __init__(self, name, inventory, profit = 0):
    self.name = name
    self.inventory = inventory
    self.profit = profit
    
  def sell_bike(self, bicycle):
    markup = bicycle.cost * 0.2
    cost = bicycle.cost + markup
    self.profit += markup
    return cost
  
class Customer(object):
  def __init__(self, name, budget):
    self.name = name
    self.budget = budget
    
  def buy_bike(self, bicycle, bike_shop):
    cost = bike_shop.sell_bike(bicycle)
    print "{} buys the {} for {} dollars".format(self.name, bicycle.model, bicycle.cost)
    self.budget -= cost
    
  def budget_remaining(self):
    print "{} has {} dollars remaining".format(self.name, self.budget)
    
sidewinder = Bicycle('tx30', 850, 20)
cheetah = Bicycle('m50', 650, 19)
clunker = Bicycle('n1', 200, 30)
merrymaker = Bicycle('m2', 100, 19)
cobra = Bicycle('t1000', 800, 18)
destroyer = Bicycle('x3', 450, 30)


johnnys = BikeShop("Johnny's", [sidewinder, cheetah, clunker, merrymaker, cobra, destroyer])
print johnnys.inventory
johnnys.sell_bike(sidewinder)

felipe = Customer("Felipe", 1050)
felipe.buy_bike(sidewinder, johnnys)
felipe.budget_remaining()

sean = Customer("Sean", 850)
sean.buy_bike(cheetah, johnnys)
sean.budget_remaining()

willie = Customer("Willie", 200)
willie.buy_bike(merrymaker, johnnys)
willie.budget_remaining()

print "Johnny's Bike Shop has made a profit of {} dollars today.".format(johnnys.profit)