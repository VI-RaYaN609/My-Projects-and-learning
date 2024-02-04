myFile = open("file.txt","a")
myFile.write("Hello")
myFile.flush()
myFile.close()

myFile = open("file.txt", "r")
line =myFile.readlines()
print(line)
myFile.close()
with open("file.txt","r") as file:
    print("This will close the file after the block of code inside \"with\" runs")