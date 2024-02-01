f = open("Diwakar.txt")
#print(f.tell()) # f.tell tells where is the file pointed at that time
print(f.readline())
#print(f.tell())
f.seek(10) # the below readlines command will start reading from 10th character, the pointer is bought to 10th position
print(f.readlines())
#print(f.tell())