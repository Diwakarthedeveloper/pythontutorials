class Father():
    def Skills(Self):
        print("I love gardening , programmim,")

class Mother():
    def Skills(Self):      
      print("I love cooking, art")

class Child(Father, Mother): # multiple inheritance is done here- resusing old code features
    def Skills(Self):   
        Father.Skills(Self)  
        Mother.Skills(Self)   
        print("I enjoy sports")

c = Child()
c.Skills()

