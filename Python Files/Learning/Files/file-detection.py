import os

Path="C:\\Users\\VI RaYaN\\Desktop\\VS Code\\Python Files\\Files\\file"

if os.path.exists(Path):
    print("location exist")
    if os.path.isfile(Path):
        print("File")
    elif os.path.isdir(Path):
        print("folder")
else :
    print("location doesn't exist")