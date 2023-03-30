from colorama import Fore
import hashlib

print(Fore.BLUE)
print("##       ##            ##            ##########  ##      ##")
print("##       ##          ##  ##         ##          ##       ##")
print("##       ##        ##     ##        ##          ##       ##")
print("###########      #############       #########  ###########")
print("##       ##    ##             ##             ## ##       ##")
print("##       ##  ##                ##            ## ##       ##")
print("##       ## ##                  ##  ########### ##       ##")
print(Fore.RED+"===========================================================")

print(Fore.RED+"Github: "+Fore.BLUE + "https://github.com/dragonwolf1o1")

project_name="Hash Calculator"
print(Fore.GREEN + project_name.center(50))

def font():
    print(Fore.GREEN + "[1] " + Fore.CYAN + "MD5")
    print(Fore.GREEN + "[2] " + Fore.CYAN + "SHA-1")
    print(Fore.GREEN + "[3] " + Fore.CYAN + "SHA-256")
    print(Fore.GREEN + "[4] " + Fore.CYAN + "SHA-512")
    print(Fore.GREEN + "[0] " + Fore.CYAN + "Exit")

font()
file_location=input("Enter the file location: ")
choose = int(input(Fore.CYAN + "Choose any one option: "))


def md5():
    md5_hash = hashlib.md5()
    with open(file_location, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            md5_hash.update(byte_block)
        print(Fore.CYAN+"Your Hash Value in MD5 is: {}".format(Fore.RED+md5_hash.hexdigest()))

def sha1():
    BLOCK_SIZE = 65536
    file_hash = hashlib.sha256()
    with open(file_location, 'rb') as f:
        fb = f.read(BLOCK_SIZE)
        while len(fb) > 0:
            file_hash.update(fb)
            fb = f.read(BLOCK_SIZE)
    print(Fore.CYAN + "Your Hash Value in SHA-1 is: {}".format(Fore.RED + file_hash.hexdigest()))

def sha256():
    sha256_hash = hashlib.sha256()
    with open(file_location, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
        print(Fore.CYAN + "Your Hash Value in SHA-256 is: {}".format(Fore.RED +sha256_hash.hexdigest()))

def sha512():
    file=file_location
    sha512_returned = hashlib.sha512(file.encode()).hexdigest()
    print(Fore.CYAN + "Your Hash Value in SHA-512 is: {}".format(Fore.RED + sha512_returned))


while choose!=0:
    if choose==1:
        md5()
        font()
        choose = int(input(Fore.CYAN+"If you try again enter the hash number:"))
        file_location = input("Enter the file location: ")
    elif choose==2:
        sha1()
        font()
        choose = int(input(Fore.CYAN+"If you try again enter the hash number:"))
        file_location = input("Enter the file location: ")
    elif choose==3:
        sha256()
        font()
        choose = int(input(Fore.CYAN+"If you try again enter the hash number:"))
        file_location = input("Enter the file location: ")
    elif choose==4:
        sha512()
        font()
        choose = int(input(Fore.CYAN+"If you try again enter the hash number:"))
        file_location = input("Enter the file location: ")
    else:
        choose=int(input(Fore.CYAN+"Please enter the correct number:"))
