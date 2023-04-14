


class dog:
	def __init__(self, name, age, coat_color):
		self.name = name
		self.age = age
		self.coat_color = coat_color

	def description(self):
		print("name of the dog is: " + self.name, "," ,"age of the dog is: " , self.age)

	def get_info(self):
		print("coat color of the dog is: " + self.coat_color)


class JackRusselTerrier(dog):
	def __init__(self, weight, eye_color):
		self.weight = weight
		self.eye_color = eye_color


	def weight_of_jrt(self):
		print("weight of JackRusselTerrier in kg is:" , self.weight)

	def eye_color_of_jrt(self):
		print("eye color of JackRusselTerrier is: " + self.eye_color)


class bulldog(dog):
	def __init__(self, country, life_expectancy):
		self.country = country
		self.life_expectancy = life_expectancy

	def country_of_bulldog(self):
		print("Origin country of the bull dog is : " + self.country)

	def life_expec(self):
		print("Life expectancy of bull dog is: " , self.life_expectancy)




obj = dog("sia", 2, "black")
obj.description()
obj.get_info()


obj2 = JackRusselTerrier(12, "black")
obj2.weight_of_jrt()
obj2.eye_color_of_jrt()


obj3 = bulldog("American", 10)
obj3.country_of_bulldog()
obj3.life_expec()                      