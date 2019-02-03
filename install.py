import os

banner = '''
___                     ______ _     _             
 | __  _ _|_ _  |  |     |  | |_|   |_)|_  o  _ |_ 
_|_| |_>  |_(_| |  |    _|_ | | |   |  | | | _> | |

'''
check_templates_modules = os.path.exists("template.tar.gz")

print(banner)
print("\033[35mInstalling ITA phish....")

if check_templates_modules ==True:
    os.system("chmod +x ngrok")
    os.system("tar zxvf template.tar.gz")
    os.system("rm template.tar.gz")
    
else:
    print("Templates Not Found !")
