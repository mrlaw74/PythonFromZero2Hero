import os
import sys
import fnmatch
# class MaxSizeList():
#     def __init__(self, value):
#         self.mylist = []
#         self.value = value

#     def pushString(self,string):
#         self.mylist.append(string)
#         pass
#     def getInfo(self):
#         print(self.mylist)
#         pass

# a = MaxSizeList(3)
# print(a)
# # print(a.pushString("Hello"))
# a.pushString("Hello")
# a.pushString("World")

# # a,pushString("Hello")
# a.getInfo()

namefile = "*.py"

def checkPath( path ):
    # check path
    if not os.path.isdir( path ):
        print ("ERROR: Path to  <" + path + "> is not a valid path.")
        sys.exit (1)

def findFiles(path):
    print ("TCDescrip.findFiles: Search for file name: " + namefile + "   in path: " + path)
    result = []

    # check the given path
    path = os.path.normpath( path )
    checkPath( path )

    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, namefile):
                result.append(os.path.join(root, name))
    return result

resultPath = os.path.dirname( os.path.realpath( __file__ ) )
# print(resultPath)
pyfile =findFiles(resultPath)

def remove_char_from_file(li):
    for i in li:
        file = open(i, 'r+')
        s = file.read().replace("OMKAR PATHAK", "nguyenluathcmut")
        file.close()
        file = open(i, 'w')
        file.write(s)
        file.close()
remove_char_from_file(pyfile)







import os
import sys
import glob
import fnmatch 



# 1 - Get current path, file
def getCurrentPath():
    # Method 1:
    # currentPath2 = os.path.dirname( os.path.realpath( __file__ ) )
    # Method 2:
    currentPath = os.getcwd()
    # /home/nul3hc/Personal/PythonMastery/Scripts
    return currentPath
def getCurrentFile():
    # Method 1:
    currentFile = os.path.abspath(__file__)
    return currentFile

# 2 - Find files in a absolute path:
def findFiles(pattern, nameOfFolder):
    results = []
    # pattern = '*.py'
    for name in os.listdir(nameOfFolder):
        # if os.path.isfile(os.path.join(nameOfPath, name)) and fnmatch.fnmatch(name, pattern):
        if fnmatch.fnmatch(name, pattern):
            results.append(name)
    return results

# 3 - Check folder, file is valid
def checkPathIsValid(nameOfFolder = './'):
    # Method 1: os.path.exists()
    isExist = os.path.exists(nameOfFolder)
    return isExist

# 4 - Create a new folder in a specific path
def createNewFolder(nameOfFolder = './NewFolder'):
    isCreated = False
    # User os.mkdir()
    if checkPathIsValid(nameOfFolder):
        print("Folder is exists currently, please create another Folder.")
    else:
        os.mkdir(nameOfFolder)
        print(f"A new folder is created in path: {nameOfFolder}")
        isCreated = True
    return isCreated

# 5 - Create new file in specific folder
def createNewFile(pathOfFile = './NewFile'):
    isCreated = False
    # User os.mkdir()
    if checkPathIsValid(pathOfFile):
        print("File is exists currently, please create another file.")
    else:
        newfile = open(pathOfFile,'w')
        newfile.close()
        print(f"A new file is created in path: {pathOfFile}")
        isCreated = True
    return isCreated

# 6 - Move files from folder 1 to folder 2
def moveFile(filename, oldPlace, newPlace):
    # Check namefile is exists in old place
    oldName = oldPlace+filename
    newName = newPlace+filename
    if not (checkPathIsValid(oldName) and checkPathIsValid(newPlace)):
        print(f"File {oldName} or {newPlace} folder is not exists.!!!\n Please check again.")
    elif oldPlace == newPlace:
        print(f"Old place is the same new place, we dont need to move file =).")
    else:
        # print(f"Moving file {filename} from {oldPlace} to {newPlace}.")
        content = delFile(oldName)
        createNewFile(newName)
        file = open(newName, 'w')
        file.write(content)
        file.close()
def moveFolder(folderName, oldPlace, newPlace):
    # Check folderName, oldPlace, newPlace is exists
    folderName += '/'
    oldname = oldPlace+folderName
    newname = newPlace+folderName
    createNewFolder(newname)
    if not (checkPathIsValid(oldname)):
        print(f"Folder {oldname} folder is not exists.!!!\n Please check again.")
    elif oldPlace == newPlace:
        print(f"Old place is the same new place, we dont need to move folder =).")
    else:
        print(f"Moving folder {oldname} from {oldPlace} to {newPlace}.")
        # List of all files in oldPlace
        listOfFile = findFiles('*', oldname)
        for i in listOfFile:
            # print(i)
            # Move files step by step
            moveFile(i, oldname, newname)
        delFolder(oldname)
    pass

# 7 - Delete files from a specific path
def delFile(filename):
    if checkPathIsValid(filename):
        content = ''
        file = open(filename, 'r')
        content+=file.read()
        file.close()
        os.remove(filename)
    else:
        print(f"File {filename} is not exists.")
    return content

# 8 - Delete folder from a specific path
def delFolder(folder_path):
    if os.path.exists(folder_path):
        # removing the file using the os.remove() method
        os.rmdir(folder_path)
    else:
        # file not found message
        print("File not found in the directory")
# Main 
if __name__ == '__main__':
    print("\nHello - This is a script processing file, folder, and more....\n")
    # currentPath = getCurrentPath()
    # print(currentPath)
    # getCurrentFile()
    # checkPathIsValid("./folder_file.py")
    # createNewFolder('./../SampleFolder1')

    # listOfFiles = findFiles('*.py', '../')
    # for i in listOfFiles:
    #     print(i)
    # for i in range(0,5):
    #     name = './newfile' + str(i) + '.txt'
    #     createNewFile(name)
    # listOfFiles = findFiles('*.txt', './')
    # for i in listOfFiles:
    #     print(i)

    # moveFile('newfile4.txt', './','../SampleFolder/')
    # moveFolder('SampleFolder', './', '../')
    

