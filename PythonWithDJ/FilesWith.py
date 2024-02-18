# When we use with command for files then open and close command for files is not required

with open("Diwakar.txt") as f:
    a = f.read(4)
    print(a)
    