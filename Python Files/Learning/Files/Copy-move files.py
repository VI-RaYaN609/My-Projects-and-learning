                                #copy
import shutil

# copyfile() = copies contents of a file
#copy() =      copyfile() + permission mode + destination can be a directory
#copy2() =      copy() + copies metadata(file's creation and modification times)

#shutil.copy("C:\\Users\\VI RaYaN\\Desktop\\VS Code\\file.txt",'copy.txt')
                                #move
import os
source = "C:\\Users\\VI RaYaN\\Desktop\\VS Code\\file.txt"
destination = "C:\\Users\\VI RaYaN\\Desktop\\VS Code\\Python Files\\Files"
destinationsource = "C:\\Users\\VI RaYaN\\Desktop\\VS Code\\Python Files\\Files\\file.txt"

try :
    if os.path.exists(destinationsource):
        print("There is a file with the same name ")
    else :
        os.replace(source,destination)
        print("File was removed succesfully")
except FileNotFoundError as error:
    print(error)
    print("File not found !!")
except Exception as error:
    print(error)
 
                       #removing files
#os.remove("copy.txt")
                       #removing repertoir
#os.rmdir()