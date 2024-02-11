import os
import shutil # will be used to move a file 
path = input("Enter your path : ")
files = os.listdir(path)

    # we will seperate file and extension using below code

for i in files:
    filename, extension = os.path.splitext(i)
    #print(filename)
    #print(extension)
    extension1 = extension[1:] # to remove . from the extenion, used slicing here

    folder_path = path+"\\"+extension1
    if os.path.exists(folder_path):
        #print("True")
        shutil.move(path+"\\"+i , path+"\\"+extension1+"\\" +i) # if extension folder exits move to it else create a new extension path
    else:
        #print("False")
        os.makedirs(folder_path)
        shutil.move(path + "\\" + i, path + "\\" + extension1 + "\\" + i)


    #print(extension1)
