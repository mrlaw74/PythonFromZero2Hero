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

