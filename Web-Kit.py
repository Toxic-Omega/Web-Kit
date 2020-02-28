import os
import time

def Menu():
    os.system("clear")
    print("""\033[31m
 ▄▀▀▄    ▄▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀█▄▄           ▄▀▀▄ █  ▄▀▀█▀▄    ▄▀▀▀█▀▀▄ 
█   █    ▐  █ ▐  ▄▀   ▐ ▐ ▄▀   █         █  █ ▄▀ █   █  █  █    █  ▐ 
▐  █        █   █▄▄▄▄▄    █▄▄▄▀          ▐  █▀▄  ▐   █  ▐  ▐   █     
  █   ▄    █    █    ▌    █   █            █   █     █        █      
   ▀▄▀ ▀▄ ▄▀   ▄▀▄▄▄▄    ▄▀▄▄▄▀          ▄▀   █   ▄▀▀▀▀▀▄   ▄▀       
         ▀     █    ▐   █    ▐           █    ▐  █       █ █         
               ▐        ▐                ▐       ▐       ▐ ▐         V1.0
               
                         \033[94mCoded By Toxic - Omega
                         
\033[32m[ \033[31m1 \033[32m] Install Apache2 (Web Server)
\033[32m[ \033[31m2 \033[32m] Install Ngrok (Port Forwarding)
\033[32m[ \033[31m3 \033[32m] Stop Apache2
\033[32m[ \033[31m4 \033[32m] Start Apache2 & Ngrok
\033[32m[ \033[31m5 \033[32m] 
\033[32m[ \033[31m6 \033[32m] 
\033[32m[ \033[31m7 \033[32m] 
\033[32m[ \033[31m8 \033[32m]   
\033[31m       
""")
loop = True
while loop:
    Menu()
    what = input("--> ")
#------------------------------------------------------------------------------
    if what == "1":
        os.system("clear")
        print("""\033[31m
 ▄▀▀▄    ▄▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀█▄▄           ▄▀▀▄ █  ▄▀▀█▀▄    ▄▀▀▀█▀▀▄ 
█   █    ▐  █ ▐  ▄▀   ▐ ▐ ▄▀   █         █  █ ▄▀ █   █  █  █    █  ▐ 
▐  █        █   █▄▄▄▄▄    █▄▄▄▀          ▐  █▀▄  ▐   █  ▐  ▐   █     
  █   ▄    █    █    ▌    █   █            █   █     █        █      
   ▀▄▀ ▀▄ ▄▀   ▄▀▄▄▄▄    ▄▀▄▄▄▀          ▄▀   █   ▄▀▀▀▀▀▄   ▄▀       
         ▀     █    ▐   █    ▐           █    ▐  █       █ █         
               ▐        ▐                ▐       ▐       ▐ ▐         V1.0
               
                         \033[94mCoded By Toxic - Omega
\033[31m
""")
        os.system("sudo apt-get install apache2")
#------------------------------------------------------------------------------
    elif what == "2":
        os.system("clear")
        print("""\033[31m
 ▄▀▀▄    ▄▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀█▄▄           ▄▀▀▄ █  ▄▀▀█▀▄    ▄▀▀▀█▀▀▄ 
█   █    ▐  █ ▐  ▄▀   ▐ ▐ ▄▀   █         █  █ ▄▀ █   █  █  █    █  ▐ 
▐  █        █   █▄▄▄▄▄    █▄▄▄▀          ▐  █▀▄  ▐   █  ▐  ▐   █     
  █   ▄    █    █    ▌    █   █            █   █     █        █      
   ▀▄▀ ▀▄ ▄▀   ▄▀▄▄▄▄    ▄▀▄▄▄▀          ▄▀   █   ▄▀▀▀▀▀▄   ▄▀       
         ▀     █    ▐   █    ▐           █    ▐  █       █ █         
               ▐        ▐                ▐       ▐       ▐ ▐         V1.0
               
                         \033[94mCoded By Toxic - Omega
\033[31m
""")
        os.system("sudo apt-get install wget")
        os.system("wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip")
        os.system("unzip ngrok-stable-linux-amd64.zip")
        os.system("sudo rm ngrok-stable-linux-amd64.zip")
#------------------------------------------------------------------------------