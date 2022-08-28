import os
import time

print("Current directory is: ", os.getcwd())        #current directory

currentDir = os.getcwd()
filename = 'result.txt'
fullPath = os.path.join(currentDir,filename)
print("\nThe constructed file path is: ", fullPath)     #constructed file

realtivePath = 'output.txt'
print("\nThe absolute path is: ",os.path.abspath(realtivePath))     #absolute path

filePath = r'c:\temp\results.txt'
print("\nThe file name part is ",os.path.basename(filePath))
print("The directory part is: ",os.path.exists(filePath))       #analize file path

print("\nIs file existing? ",os.path.exists(filePath))      #is file exists?

if os.path.exists(filePath):
    print("\nLast modify date is: ", os.path.getmtime(filePath))        #last modify time
    print("Last modify date is: ",time.localtime(os.path.getmtime(filePath)))

    print("\nFile size is", os.path.getsize(filePath))      #file size (bytes)

    print("\nIs it a file?",os.path.isfile(filePath))       #is it file?
    print("Is it a dir? ",os.path.isdir(filePath))          #is it dir?

    print("\nPath splitted", os.path.isfile(filePath))      #cut last part of file path
    print("Only file name part:",os.path.split(filePath)[1])    #cut the chosen part of file path

    print("\nPath splitted into dribe", os.path.splitdrive(filePath))       #cut drive name
    print("Only drive:", os.path.splitdrive(filePath)[0])


print("\n-----------------------------------------")

dir = input("Enter directory name: ")

if not os.path.isdir(dir):
    print("%s must be a directory" % dir)
else:
    file = input("Please enter file name saved in directory %s: " % dir)
    path = os.path.join(dir, file)

    if os.path.exists(path):
        print("Last modify date is: ", time.localtime(os.path.getmtime(path)))
        print("File size is", os.path.getsize(path))
        print("Current directory is: ", os.getcwd())
        print("The constructed file path is: ", path)
    else:
        print('File %s does not exist!' % path)
