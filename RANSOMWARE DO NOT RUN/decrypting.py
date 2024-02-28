from cryptography.fernet import Fernet
import os

directory="c:\\Users\\VI RaYaN\\Desktop\\VS Code\\RANSOMWARE DO NOT RUN"
files = []
for file in os.listdir(directory):
    if file == 'RansomWare.py'or file== 'key.txt'or file=='decrypting.py'or file=='ransomware2.py':
        continue
    if os.path.isfile(directory+"\\"+file):
        files.append(file)

with open(directory+"\\key.txt","rb") as thefile :
    key=thefile.read()

for file in files:
    with open(directory+"\\"+file,"rb") as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(key).decrypt(contents)
    with open(directory+"\\"+file ,"wb") as thefile:
        thefile.write(contents_decrypted)