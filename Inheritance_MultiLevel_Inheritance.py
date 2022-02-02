class GrandFather:
    stick = "Another leg"
    def A(self):
        print("This is GrandFather's Property")

    def E(self):
        print("this is method E of GrandFather class")

class Father(GrandFather):
    pen = "Reynold's pen"
    def B(self):
        print("This is Father's Property")

    def Hyd(self):
        print("This is father's city Hyderabad")

class Son(Father):
    mobile = "realme"
    def C(self):
        print("This is Son's Property")

gf = GrandFather()
f = Father()
s = Son()

s.A()