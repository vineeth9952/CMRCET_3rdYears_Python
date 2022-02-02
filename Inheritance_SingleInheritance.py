class Dad:
    def Show(self):
        print("This is Dad's Property")

class Son(Dad):
    pass

s = Son()
s.Show()