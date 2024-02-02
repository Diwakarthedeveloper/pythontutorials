#there ar many exceptions in pythin check official documentations

try:
    
    raise MemoryError('memory error') #MemortError is a builtin specific exception type for python
    #raise Exception('memory error')
except MemoryError as e :  # Exception can also be used as a genric exception instead of specific exception 
#except Exception as e :
    print(e)

    # how to define your own exception ?
    #ans: exceptions in python are actually instances of classes , 
    # so to define a exceptosn we nee dto define a class