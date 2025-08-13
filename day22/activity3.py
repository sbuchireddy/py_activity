class Vehicle:
	def __init__(self, brand):
		self.brand = brand

	def start(self):
		print(self.brand,"vehicle is starting")

class Car(Vehicle):
	def start(self):
		print(self.brand,"car engine starts")

class Bike(Vehicle):
	def start(self):
		print(self.brand,"bike engine starts")
#Creating instances of subclasses
vehicles = [Car("Swift"), Bike("Honda")]

for v in vehicles:	
    v.start()

