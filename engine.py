''' this antivirus is created by  Yogeshwar saini 
    in this antivirus database is used by ANIC'''

import hashlib
import os

# global variable
malware_hashes = list(open("D:\\antivirus programs\\virus hash.txt","r").read().split('\n'))
virusinfo = list(open("D:\\antivirus programs\\virusinfo.txt","r").read().split('\n'))

# get hash of a file
def sha256_hash(filename):
    try:
    
        with open(filename, "rb") as f:
            bytes = f.read()
            sha256hash = hashlib.sha256(bytes).hexdigest()
            
            f.close()
            # print(sha256hash)

        return sha256hash
    except:
        return 0

# malware detection by hash
def malware_checker(pathofFile):
    global malware_hashes
    global virusinfo
    hash_malware_check = sha256_hash(pathofFile)
    counter = 0

    for i in malware_hashes:
        if i ==hash_malware_check:
            return virusinfo[counter]
        counter+=1

    return 0
# malware detection in folder
#  list of files
virusName=[]
virusPath=[]


def folderScanner():
    dir_list=list()
    # get the list of all files and directories
    for(dirpath,dirnames,filenames)in os.walk("C:\\Program Files (x86)"):
        dir_list +=[os.path.join(dirpath , file)for file in filenames]
        
    for i in dir_list :
        print(i)
        if malware_checker(i) !=0:
            virusName.append(malware_checker(i)+ ":: File ::"+i)
folderScanner()
print(virusName)
 
def virusScanner(path):
    dir_list = list()
    for(dirpath,dirnames,filenames) in os.walk(path):
        dir_list += [os.path.join(dirpath, file) for file in filenames]
    
    for i in dir_list:
        
        if malware_checker(i)!= 0:
            print(i)
            virusName.append(malware_checker(i)+" :: File :: "+ i)
            virusPath.append(i)

#virus Remover
def virusRemover(path):
    virusScanner(path)
    if virusPath:
        for i in virusPath:
            os.remove(i)
    else:
        return 0
    
    
    
    
    # print(" total junk file is removed : -")
def junkFileRemover():
    # temp file remover 
    
    temp_list = list()
    
    # Window username
    
    username = os.environ.get('USERNAME').upper().split(" ")     # fix the file path   ###########################
    # print(username)
        
    for(dirpath,dirnames,filenames) in os.walk("C:\\Windows\\Temp"):
        temp_list += [os.path.join(dirpath, file) for file in filenames]
        temp_list += [os.path.join(dirpath,file) for file in dirnames]
        
    for(dirpath,dirnames,filenames) in os.walk("C:\\Users\\{}~1\\AppData\\Local\\Temp".format(username[0])):     #   fix the file path   #
        temp_list += [os.path.join(dirpath, file) for file in filenames]
        temp_list += [os.path.join(dirpath,file) for file in dirnames]
        
    for(dirpath,dirnames,filenames) in os.walk("C:\\Windows\\Prefetch"):
        temp_list += [os.path.join(dirpath, file) for file in filenames]
        temp_list += [os.path.join(dirpath,file) for file in dirnames]
        
    print(temp_list)   
        
    # print(" total junk file is removed : -")
    
    
    
    if temp_list:
       
        for i in temp_list:
            print(i)
            try:
                os.remove(i)
                
            except:
                pass
    else:
        return 0

    print(temp_list)
    
    
    


########################        ram boosting       #######################
# def rambooster():
    
#     taskList = ["notepad.exe" , "chrome.exe","AnyDesk.exe","cmd.exe","powershell.exe"," tasklist.exe","waterfox.exe"," edge.exe ","tor.exe",
#                 "WindowsTerminal.exe","firefox.exe"," Code.exe","vmware-tray.exe","msedge.exe ","OneDrive.exe","WhatsApp.exe ","Windows.Media.BackgroundP "," explorer.exe"
#                 ," services.exe" ," AlienFXSubAgent.exe" , " paint.exe ","telegram.exe","youtube.exe"]
#     # taskkill
#     print(" all task has been killed ")
#     for i in taskList:
#         try:
            
#             os.system("taskkill /f /im  {}".format(i) )
        
#         except:
#             return 0
                      
    
# rambooster()