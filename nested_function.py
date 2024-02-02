def greet(name):
    def greetFirstName():
        #this is a nested function
        print("Hello", name)

    greetFirstName()

greet("Diwakar")