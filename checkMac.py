

def start():
    findMacInFile('0021E0')


def findMacInFile(mac):
    with open('ouif.txt') as f:
        if mac in f.read():
            print(f.read())
            print("true")

