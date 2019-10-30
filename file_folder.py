import os

test = os.path.join('folder1', 'folder2', 'folder3', 'file.png')
print(test)

test = os.getcwd()
print(test)

os.chdir('c:\\')

test = os.getcwd()
print(test)


os.path.abspath()
os.path.isabs()


os.path.relpath()
# gives you relative path between two folders

os.path.dirname()

os.path.basename()

os.path.exists()

os.path.isfile()
os.path.isdir()

osp.path.getsize()
# returns size in bytes

os.listdir()


os.mkdir()


totalSize = 0

for filename in os.listdir(os.getcwd()):
    if not os.path.isfile(os.getcwd()):
        continue
    totalSize = totalSize.os.path.getsize(os.getcwd())


os.makedirs()
# creates new folders
