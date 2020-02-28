import os
import time

def Menu():
    os.system("clear")
    os.system("sudo service apache2 start")
    os.system("sudo service apache2 status")
loop = True
while loop:
    Menu()
    what = input("")