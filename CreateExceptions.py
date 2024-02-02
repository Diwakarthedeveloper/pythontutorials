# how to define your own exception ?
    #ans: exceptions in python are actually instances of classes , 
    # so to define a exceptosn we nee dto define a class

class Accident(Exception): #accident is self defined derived from Exception class.
    def __init__(self,msg):
        self.msg=msg
    def print_exception(self):
        print("User difined exception: " , self.msg)

try:
    raise Accident('crasg between 2 cars')
except Accident as e:
    e.print_exception()

    #----------------------------------------------------------------------------
    def process_file():
        try:
            f=open("D:\\python learning\\funny_wc.txt")
            x=1/0  # this exception- we will not handl but will clear file contents using finally
        except FileNotFoundError as e:
            print("inside except")
        finally:
            print("cleaning up file") # finally will always execute even if exceptions are not handled
            f.close

process_file()