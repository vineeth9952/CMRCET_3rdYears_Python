class Food:
    Restuarent = "CMR Canteen"
    def __init__(self,starter,maincourse,dessert):
        self.starter = starter
        self.maincourse = maincourse
        self.dessert = dessert

    def show(self):
        print(self.starter, self.maincourse, self.dessert)

    @classmethod #decorator
    def place(cls,a):
        cls.Restuarent = a
        return Food.Restuarent

meal1 = Food("chicken_tikka","Biryani","gualb_jamun")
meal2 = Food("Manchuriyan","Mutton_biryani","Icecream")

print(Food.place("Platfor65"))

'''
===> class methods are bounded to class not to the Object of class
===> class methods can modify a class state that would apply across all
        the instances of the class
'''