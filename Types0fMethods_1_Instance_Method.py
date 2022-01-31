class Food:
    def __init__(self,starter,maincourse,dessert):
        self.starter = starter
        self.maincourse = maincourse
        self.dessert = dessert

    def show(self):
        print(self.starter, self.maincourse, self.dessert)

    def get_maincourse(self):#getter method or Accessor
        return self.maincourse

    def set_maincourse(self,newmaincourse):
        self.maincourse = newmaincourse


meal1 = Food("chicken_tikka","Biryani","gualb_jamun")
meal2 = Food("Manchuriyan","Mutton_biryani","Icecream")

print(meal1.get_maincourse())
meal1.set_maincourse("Fish_man")
print(meal1.get_maincourse())

