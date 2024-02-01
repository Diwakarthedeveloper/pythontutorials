class Human:   #Human is a class
    def __init__(self, n, o):
        self.name = n   # name and occupation are properties
        self.occupation = o
# below do_work and speaks are methods

    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name,"play tennis")
        elif self.occupation == "actor" :
            print(self.name,"shoots a film")

    def speaks(self):
            print(self.name,"says how are you")


diwakar = Human("Diwakar Jha","tennis player")
diwakar.do_work()
diwakar.speaks()

maria = Human("Maria Sharapoa","actor")
maria.do_work()
maria.speaks()
