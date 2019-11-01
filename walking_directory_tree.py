import os

for folderName, subfolders, filenames in os.walk('C:\Program Files\Python37\Scripts'):
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
    print('The filenames in ' + folderName + ' are: ' + str(filenames))
    print()

    for subfolder in subfolders:
        if 'fish' in subfolder:
            # os.rmdir(subfolder)
            print('rmdir on ' + subfolder)

    for file in filenames:
        if file.endswith('.py'):
            # shutil.copy(os.jion(folderName, file) os.join( folderName, file + '.backup'))
