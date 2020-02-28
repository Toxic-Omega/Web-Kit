import os
import time

def Menu():
    os.system("sudo service apache2 start")
    os.system("clear")
    os.system("sudo service apache2 status")
    print("If Apache Is Not Running Then Start It!")
loop = True
while loop:
    Menu()
    what = input("")