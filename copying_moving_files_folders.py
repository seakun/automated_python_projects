import shutil

# copy
shutil.copy('C:\\Users\\skung.QUANTUMMANAGEME\\Documents\\hello.txt', 'C:\\')

# copy and rename to spam.txt
shutil.copy('C:\\Users\\skung.QUANTUMMANAGEME\\Documents\\hello.txt', 'C:\\spam.txt')

shutil.copyTree('C:\\Users\\skung.QUANTUMMANAGEME\\Documents\\','C:\\Users\\skung.QUANTUMMANAGEME\\Documents_backup')
#copy folder and all its content

shutil.move(src, dest)

#rename - use move function to move it in the same folder with a new name
shutil.move(src, dest)


                
