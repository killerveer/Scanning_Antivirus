# # # # 
# # # import os

# # # import win32file
# # # import win32con
# # # import engine

# # # def RealTime(): 

# # #   usernameUp = os.environ.get('USERNAME').upper().split(" ")
# # #   username = os.environ.get('USERNAME')

# # #   ACTIONS = {
# # #     1 : "Created",
# # #     2 : "Deleted",
# # #     3 : "Updated",
# # #     4 : "Renamed from something",
# # #     5 : "Renamed to something"
# # #   }

# # #   FILE_LIST_DIRECTORY = 0x0001

# # #   path_to_watch = "C:\\"
# # #   hDir = win32file.CreateFile (
# # #     path_to_watch,
# # #     FILE_LIST_DIRECTORY,
# # #     win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
# # #     None,
# # #     win32con.OPEN_EXISTING,
# # #     win32con.FILE_FLAG_BACKUP_SEMANTICS,
# # #     None
# # #   )
# # #   while 1:
  
# # #     results = win32file.ReadDirectoryChangesW (
# # #       hDir,
# # #       1024,
# # #       True,
# # #       win32con.FILE_NOTIFY_CHANGE_FILE_NAME |
# # #       win32con.FILE_NOTIFY_CHANGE_DIR_NAME |
# # #       win32con.FILE_NOTIFY_CHANGE_ATTRIBUTES |
# # #       win32con.FILE_NOTIFY_CHANGE_SIZE |
# # #       win32con.FILE_NOTIFY_CHANGE_LAST_WRITE |
# # #       win32con.FILE_NOTIFY_CHANGE_SECURITY,
# # #       None,
# # #       None
# # #     )

# # #     paths = [] 
  
# # #     for action, file in results:
# # #       paths.append(os.path.join (path_to_watch, file))
    
# # #       if paths[0][0:32] == "C:\\Users\\{}\\AppData\\".format(username):paths.clear()
# # #       elif paths[0][0:18] == "C:\\Users\\{}~1\\".format(usernameUp[0]):paths.clear()
# # #       elif paths[0][0:20] == "C:\\Windows\\Prefetch\\":paths.clear()
# # #       elif paths[0][0:15] == "C:\\Windows\\Temp":paths.clear()
# # #       elif paths[0][0:15] == "C:\\$Recycle.Bin":paths.clear()
# # #       elif paths[0][0:14] == "C:\\ProgramData":paths.clear()
# # #       elif paths[0][0:23] == "C:\\Windows\\ServiceState":paths.clear()
# # #       elif paths[0][0:15] == "C:\\Windows\\Logs":paths.clear()
# # #       elif paths[0][0:26] == "C:\\Windows\\ServiceProfiles":paths.clear()
# # #       elif paths[0][0:19] == "C:\\Windows\\System32":paths.clear()
# # #       elif paths[0][0:28] == "C:\\Program Files\\CUAssistant":paths.clear()
# # #       elif paths[0][0:23] == "C:\\Windows\\bootstat.dat":paths.clear()

# # #       # try:print (paths[0], ACTIONS.get (action, "Unknown"))
# # #       # except:pass
# # #       try:engine.virusScanner(paths[0])
# # #       except:pass
# # #       paths.clear()

# # #     with open("real-time_switch.blink",'r') as blinkswitch:
# # #       switch = blinkswitch.read()
# # #       blinkswitch.close()
  
# # #     if switch == "0" or switch == None or switch == "":
# # #       exit()
    

# # # RealTime()




# # '''This Antivirus Created By Dr.Nick_Z (Manish Parihar)
# #     In This Antivirus DataBase Is used By Anic.'''

# # import hashlib
# # import os

# # #Global Variable
# # malware_hashes = list(open("virusHash.unibit","r").read().split('\n'))
# # virusInfo = list(open("virusInfo.unibit","r").read().split('\n'))


# # #Get Hash Of File
# # def sha256_hash(filename):
# #     try:
# #         with open(filename,"rb") as f:
# #             bytes = f.read()
# #             sha256hash = hashlib.sha256(bytes).hexdigest()

# #             f.close()
# #         # print(sha256hash)
# #         return sha256hash
# #     except:
# #         return 0
    
# # #Malware Dectection By Hash
# # def malware_checker(pathOfFile):
# #     global malware_hashes
# #     global virusInfo
    
# #     hash_malware_check = sha256_hash(pathOfFile)
# #     counter = 0


# #     for i in malware_hashes:
# #         if i == hash_malware_check:
# #             return virusInfo[counter]
# #         counter += 1

# #     return 0


# # #Malware Dectection In Folder
# # virusName = []
# # virusPath = []

# # def virusScanner(path):

# #     # Get the list of all files in directory tree at given path
# #     dir_list = list()
# #     for (dirpath, dirnames, filenames) in os.walk(path):
# #         dir_list += [os.path.join(dirpath, file) for file in filenames]

# #     for i in dir_list:
# #         if malware_checker(i) != 0:
# #             print(i)
# #             virusName.append(malware_checker(i)+" :: File :: "+i)
# #             virusPath.append(i)


# # # Virus Remover
# # def virusRemover(path):
# #     virusScanner(path)
# #     if virusPath:
# #         for i in virusPath:
# #             os.remove(i)
# #     else:
# #         return 0
 


# # def juckFileRemover():

# #     # Temp Files Remover

# #     temp_list = list()

# #     # Windows username

# #     username = os.environ.get('USERNAME').upper().split(" ")

# #     for (dirpath, dirnames, filenames) in os.walk("C:\\Windows\\Temp"):
# #         temp_list += [os.path.join(dirpath, file) for file in filenames]
# #         temp_list += [os.path.join(dirpath, file) for file in dirnames]

# #     for (dirpath, dirnames, filenames) in os.walk("C:\\Users\\{}~1\\AppData\\Local\\Temp".format(username[0])):
# #         temp_list += [os.path.join(dirpath, file) for file in filenames]
# #         temp_list += [os.path.join(dirpath, file) for file in dirnames]
        

# #     for (dirpath, dirnames, filenames) in os.walk("C:\\Windows\\Prefetch"):
# #         temp_list += [os.path.join(dirpath, file) for file in filenames]
# #         temp_list += [os.path.join(dirpath, file) for file in dirnames]


# #     if temp_list:
        
# #             for i in temp_list:
# #                 print(i)

# #                 try:
# #                     os.remove(i)

# #                 except:
# #                     pass

# #                 try:
# #                     os.rmdir(i)

# #                 except:
# #                     pass
        
        

# #     else:
# #         return 0


# # def ramBooster():

# #     taskList = ["notepad.exe","AnyDesk.exe","TeamViewer_Service.exe","msedge.exe","IDMan.exe",]

# #     # Task Kill

# #     for i in taskList:

# #             os.system("taskkill /f /im  {}".format(i))


# from tkinter import *
# from tkinter import filedialog
# import random
# import os
# import time
# import engine

# os.startfile("real-time-protection_setting.bat")

# window = Tk()

# window.title("BitLink Aqua")
# window.geometry('1100x600')
# window.maxsize("1100","600")
# window.minsize("1100","600")

# nj = Frame(window, width=1100, height = 600)
# nj.pack()
# nj.pack_propagate(0)

# def mainFrameNj():

#     global opring
#     global quickScanImg
#     global junkFileRemoverImg
#     global ramBoosterImg
#     global photoScan
#     global nj

#     nj.destroy()

#     nj = Frame(window, width=1100, height = 600)
#     nj.pack()
#     nj.pack_propagate(0)



#     def junkFileRemoverFunc():
#         ri = engine.juckFileRemover
#         ri()

#     def ramBoosterFunc():
#         ri = engine.ramBooster
#         ri()

#     def customScanFunc():
#         source_path = filedialog.askdirectory(title='Select the Parent Directory')
#         print(source_path)
#         ri = engine.virusScanner
#         ri(source_path)

#     def writeFile(write):
#         switch_check = open("real-time_switch.blink","w")
#         switch_check.write(write)
#         switch_check.close()

#     def AV_switch():
#         switch_check = open("real-time_switch.blink","r")
#         Pos = switch_check.readline()
#         switch_check.close()    
    

#         if Pos == 1 or Pos == "1" :
#             print(Pos)
#             writeFile("0")
        
#             tls.configure(image = photog)
        
    
#         elif Pos == 0 or Pos == "0":
#             print(Pos)
#             writeFile("1")
        
#             tls.configure(image = photoi)

#     opring = 5

#     def buleAnimation_():
#         global opring

#         buleAnimationPlus00.configure(image = buleAnimationPlusList[opring])


#         if opring == 0:
#             opring = 5

#         opring -= 1

#         buleAnimationPlus00.after(200,buleAnimation_)



#     photoi = PhotoImage(file = "res\\0.png").subsample(3,3)
#     photog = PhotoImage(file = "res\\0 a.png").subsample(3,3)
#     photoScan = PhotoImage(file = "res\\scan l.png").subsample(4,4)
#     junkFileRemoverImg = PhotoImage( file = "res\\junk file remover.png").subsample(4,4)
#     quickScanImg = PhotoImage(file ="res\\quick scan.png").subsample(4,4)
#     ramBoosterImg = PhotoImage(file = "res\\ram booster.png").subsample(4,4)

#     buleAnimationPlus0 = PhotoImage( file = "res\\blue ani\\0.png").subsample(21,21)
#     buleAnimationPlus1 = PhotoImage( file = "res\\blue ani\\1.png").subsample(21,21)
#     buleAnimationPlus2 = PhotoImage( file = "res\\blue ani\\2.png").subsample(21,21)
#     buleAnimationPlus3 = PhotoImage( file = "res\\blue ani\\3.png").subsample(21,21)
#     buleAnimationPlus4 = PhotoImage( file = "res\\blue ani\\4.png").subsample(21,21)
#     buleAnimationPlus5 = PhotoImage( file = "res\\blue ani\\5.png").subsample(21,21)


#     buleAnimationPlusList = [buleAnimationPlus0,buleAnimationPlus1,buleAnimationPlus2,buleAnimationPlus3,buleAnimationPlus4,buleAnimationPlus5]




#     bitLinkMainLabel = Label(nj, text = "BitLink Aqua", font = "Times 30 bold")
#     bitLinkMainLabel.pack(side = TOP, pady = 20)

#     tls = Button(nj, text = 'Click Me !', image = photoi, bd=0, command=AV_switch)
#     tls.pack(side = TOP, pady = 0)

#     quickScan = Button(nj, image = quickScanImg, bd = 0, command = quickScanFrame)
#     quickScan.place( x = 90 , y = 410)
    
#     fscan = Button(nj, image = photoScan, bd = 0, command = customScanFunc)
#     fscan.place(x = 350 , y = 410)

#     junkFileRemover = Button(nj, image = junkFileRemoverImg ,bd = 0, command = junkFileRemoverFunc)
#     junkFileRemover.place( x = 610 , y = 410)

#     ramBooster = Button(nj, image = ramBoosterImg , bd = 0, command = ramBoosterFunc)
#     ramBooster.place( x = 870 , y = 410)

#     buleAnimationPlus00 = Label(nj, image = buleAnimationPlus0)
#     buleAnimationPlus00.place(x = 50, y = 10)

#     buleAnimation_()


# def quickScanFrame():
#     global nj
#     global backButtonImg
#     global prog0
#     global prog1
#     global prog2
#     global prog3
#     global prog4
#     global prog5
#     global io
#     global ranHashShower
#     global samB
#     global rMVirus

#     with open("virusHash.unibit", "r") as nr:
#         samB = nr.readlines()
#         nr.close()



#     nj.destroy()

#     nj = Frame(window, width=1100, height = 600)
#     nj.pack()
#     nj.pack_propagate(0)

#     io = 0

#     def removeVirusBtn():
#         try : 
#             with open("switch_virusscanner.bb","r") as bb:
#                 io = list(bb.readlines())
#                 bb.close()
#         except:pass

#         try:
#             for i in io:
#                 i = i[0:len(i)-1]
#                 print(i," Removed")
#                 os.remove(i)
#         except:pass


#     def progressBarAni():
#         global io
        
#         progLabel.configure(image = progList[io])

#         io += 1

        

#         id = progLabel.after(500, progressBarAni)

#         if io == 5:
#             io = 0
#             try : 
#                 with open("switch_io.bb","r") as nri:
#                     xxc = nri.read()
#                     nri.close()
                
#                 if xxc == "1" or xxc == 1:
#                     progLabel.after_cancel(id)
            
#             except:pass

#     def textShower():
#         global samB

#         ranHashShower.configure(state='normal')
#         ranHashShower.delete("1.0",END)
#         ranHashShower.insert(INSERT,samB[random.randint(0,len(samB)-1)])

#         id = ranHashShower.after(100, textShower)

#         try : 
#             with open("switch_io.bb","r") as nri:
#                 xxc = nri.read()
#                 nri.close()
                
#             if xxc == "1" or xxc == 1:
#                 ranHashShower.after_cancel(id)
            
#         except:pass

#     def VirusFoundPathX():

#         try:
#             with open ("switch_virusscanner.bb","r") as X:
#                 cc = X.readlines()
#                 X.close()
        

#             virusFoundPaths.configure(state='normal')
#             virusFoundPaths.delete("1.0",END)
#             virusFoundPaths.insert(INSERT,cc)


#         except:pass

#         id = virusFoundPaths.after(200, VirusFoundPathX)

#     backButtonImg = PhotoImage(file = "res\\back button.png").subsample(4,4)
#     prog0 = PhotoImage( file = "res\\progress bar\\0.png").subsample(1,3)
#     prog1 = PhotoImage( file = "res\\progress bar\\1.png").subsample(1,3)
#     prog2 = PhotoImage( file = "res\\progress bar\\2.png").subsample(1,3)
#     prog3 = PhotoImage( file = "res\\progress bar\\3.png").subsample(1,3)
#     prog4 = PhotoImage( file = "res\\progress bar\\4.png").subsample(1,3)
#     prog5 = PhotoImage( file = "res\\progress bar\\5.png").subsample(1,3)
#     progList = [prog0,prog1,prog2,prog3,prog4,prog5]

#     bitLinkMainLabel = Label(nj, text = "Quick Scan", font = "Times 21 bold")
#     bitLinkMainLabel.pack(side = TOP, pady = 20)

#     backButton = Button(nj, image = backButtonImg, bd = 0, command = mainFrameNj)
#     backButton.place(x = 10 , y = 10)

#     progLabel = Label(nj, image = prog0)
#     progLabel.place(x = 250, y = 70)


#     pathLabel = Label(nj, text = "Virus Scanner", font = "Times 20 bold")
#     pathLabel.place(x = 350, y = 130)

#     ranHashShower = Text(nj, width=50, height=1, bd = 0, font= ('Sans Serif', 13, 'bold'),foreground="green")
#     ranHashShower.place( x = 350 , y = 170)
#     ranHashShower.insert(INSERT, "Write Something About Yourself")
#     ranHashShower.configure(state='disabled')

#     virusDetet = Label(nj, text = "Virus Found", font = "Times 20 bold")
#     virusDetet.place(x = 350, y = 230)

#     virusFoundPaths = Text(nj, width=100, height=10, bd = 0, font= ('Sans Serif', 13, 'bold'),foreground="red")
#     virusFoundPaths.place( x = 50 , y = 290)
#     virusFoundPaths.insert(INSERT, "No Virus Found")
#     virusFoundPaths.configure(state='disabled')

#     rMVirus = Button(nj, text = "Remove Virus", font = "Times 20 bold", command = removeVirusBtn)
#     rMVirus.place(x = 350, y = 230)

#     textShower()

#     progressBarAni()

#     os.startfile("scannerStartQuick.bat")

#     VirusFoundPathX()


#     # Get the list of all files in directory tree at given path

        




# mainFrameNj()





# window.mainloop()



