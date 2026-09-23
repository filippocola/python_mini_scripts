import os 
from pathlib import Path

if __name__ == "__main__":
    rowCount = 0
    path = Path("files", "file.txt")
    print("PATH:", path)
    with open("./file.txt", "r+") as fs:
        culi = fs.readlines()
        for culo in culi:
            print("Culo N° " + str(rowCount )) 
            rowCount += 1

    fs.close()