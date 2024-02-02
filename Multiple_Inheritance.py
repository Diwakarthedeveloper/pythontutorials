class Father():
    def gardening(Self):
        print("I enjoy gardening ")

class Mother():
    def cooking(self):
        print("I love cooking")

class Child(Father, Mother): # multiple inheritance is done here- resusing old code features
    def sports(Self):
        print("I enjoy sports")

c = Child()
c.gardening()
c.cooking()
c.sports()

