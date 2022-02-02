class Father:
    a = "wallet"
    def show(self):
        print("Father have strict mentality yet they are caring.")

class Mother:
    b = "love"
    def show(self):
        print("Mother are kind yet they scold us.")

class son(Mother,Father):
    c = "wastetime"
    def Innocent(self):
        print("son looks like he is innocent but actually he is not.")


s = son()
s.show()
