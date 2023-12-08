# imports ###############################################################
from glob import glob
from tkinter import *
import psutil


import pystray
import PIL.Image
from screeninfo import get_monitors

#------------------------global variable------------------------------#



#------------------------global variable end--------------------------#



# ---------------------- TKinter base setup---------------------------#

window= Tk()
window.title(" The Dead Beast(FFU Antivirus) ")
window.geometry("1400x600+350+150")
window.maxsize(900,660)
window.minsize(900,660)

winFrame = Frame(window,width="900",height="650",bg="black")
winFrame.pack()
winFrame.pack_propagate()

title_bar = Frame(window,bg='gray17' , relief='raised')
title_bar.pack(expand=1, fill=X)

def CloseWindow(event):
    window.overrideredirect(True)
    window.withdraw()

    def OpenWindow():
        window.deiconify()
        window.overrideredirect(True)
        iconIo.stop()

    ioIconImage = PIL.Image.open("D:\\antivirus programs\\BitLink\\Bit-Link Antivirus Pro Working\\res\\Logo\\logo.ico")
    iconIo = pystray.Icon("logo",ioIconImage,menu=pystray.Menu(pystray.MenuItem("Open", OpenWindow,default=True)))
    iconIo.run()

def CloseButtonEnter(event):
    close_button.config(image=close_buttonImgHoved)

def CloseButtonLeave(event):
    close_button.config(image=close_buttonImg)

close_buttonImg =PhotoImage(file="D:\\antivirus programs\\BitLink\\Bit-Link Antivirus Pro Working\\res\\Title Bar\\close non-hoved.png").subsample(2,2)
close_buttonImgHoved = PhotoImage(file="D:\\antivirus programs\\BitLink\\Bit-Link Antivirus Pro Working\\res\Title Bar\\close hoved.png").subsample(2,2)
close_button = Label(title_bar, cursor="hand2",image=close_buttonImg,bg='gray17')
close_button.pack(side=RIGHT)
close_button.bind('<Button-1>',CloseWindow)
close_button.bind('<Enter>',CloseButtonEnter)
close_button.bind('<Leave>',CloseButtonLeave)

def MinimizeWindow(event):
    window.overrideredirect(False)
    window.iconify()

def MinimizeButtonEnter(event):
    minimize_button.config(image=minimize_buttonImgHoved)

def MinimizeButtonLeave(event):
    minimize_button.config(image=minimize_buttonImg)


minimize_buttonImg = PhotoImage(file="D:\\antivirus programs\BitLink\\Bit-Link Antivirus Pro Working\\res\Title Bar\\minimize non-hoved.png").subsample(2,2)
minimize_buttonImgHoved = PhotoImage(file="D:\\antivirus programs\\BitLink\\Bit-Link Antivirus Pro Working\\res\\Title Bar\\minimize hoved.png").subsample(2,2)
minimize_button = Label(title_bar, cursor="hand2",image=minimize_buttonImg,bg='gray17')
minimize_button.pack(side=RIGHT)
minimize_button.bind('<Button-1>',MinimizeWindow)
minimize_button.bind('<Enter>',MinimizeButtonEnter)
minimize_button.bind('<Leave>',MinimizeButtonLeave)

def MaximizeScreen(event):
    window.overrideredirect(True)
    window.deiconify()

title_bar.bind('<Map>',MaximizeScreen)




def get_pos(event):
    xwin = window.winfo_x()
    ywin = window.winfo_y()
    startx = event.x_root
    starty = event.y_root

    ywin = ywin - starty
    xwin = xwin - startx

    def move_window(event):
        window.geometry("1200x850" + '+{0}+{1}'.format(event.x_root + xwin, event.y_root + ywin))

    startx = event.x_root
    starty = event.y_root

    title_bar.bind('<B1-Motion>', move_window)


title_bar.bind('<Button-1>', get_pos)

window.overrideredirect(True)  # turns off title bar, geometry
window.geometry('1200x850+30+30')





#------------------------TKinter base setup end ----------------------#

def HomeviewDarkTheme():

    # --------------------------global variable ------------------------#
    global winFrame


    # -------------------------global var EEnd -----------------------#

    winFrame.destroy()
    #------------------------main Frame ------------------------------#

    winFrame=Frame(window,width="900",height="660",bg="lightgreen")          # for frame color #
    winFrame.pack()
    winFrame.pack_propagate()
    # "D:\antivirus code\res\Blue Asset\White theme\Buttons\Hoved\hovHome.png"
    #-----------------------mainFrame end ----------------------------#

    # -----------------------------home button-------------------------#

    homeButtonImg = PhotoImage(file="D:\\antivirus programs\\Bit-Link Antivirus Yt\\res\\Buttons\\Non-Hoved\\home.png")
    hovhomeButtonImg = PhotoImage(file="D:\\antivirus programs\\Bit-Link Antivirus Yt\\res\\Buttons\\Hoved\\hovHome.png")

    def HomeButtonEnterFrame(event):
        homeButton.config(image=hovhomeButtonImg)

    def HomeButtonLeaveFrame(event):
        homeButton.config(image=homeButtonImg)

    homeButton = Label(winFrame,image=homeButtonImg,bg="black",cursor="hand2")
    homeButton.place(x=10,y=430)

    homeButton.bind('<Enter>', HomeButtonEnterFrame)
    homeButton.bind('<Leave>', HomeButtonLeaveFrame)

    # ------------------------Home Button End ------------------#
    # ------------------------scan Button ---------------------#


    scanButtonImg = PhotoImage(file="D:\\antivirus programs\\Bit-Link Antivirus Yt\\res\\Buttons\\Non-Hoved\\scan.png")
    hovScanButtonImg = PhotoImage(file="D:\\antivirus programs\\Bit-Link Antivirus Yt\\res\\Buttons\\Hoved\\hovScan.png")

    def ScanButtonEnterFrame(event):
        scanButton.config(image=hovScanButtonImg)

    def ScanButtonLeaveFrame(event):
        scanButton.config(image=scanButtonImg)

    scanButton=Label(winFrame,image=scanButtonImg,bg="black",cursor="hand2")
    scanButton.place(x=185,y=430)

    scanButton.bind('<Enter>', ScanButtonEnterFrame)
    scanButton.bind('<Leave>', ScanButtonLeaveFrame)

    # ------------------scan Button End-------------------------#

    # ------------------health Button --------------------------#

    systemButtonImg = PhotoImage(file="D:\\antivirus programs\\Bit-Link Antivirus Yt\\res\\Buttons\\Non-Hoved\\system.png")
    hovSystemButtonImg = PhotoImage(file="D:\\antivirus programs\\Bit-Link Antivirus Yt\\res\\Buttons\\Hoved\\hovSystem.png")

    def SystemButtonEnterFrame(event):
        systemButton.config(image=hovSystemButtonImg)

    def SystemButtonLeaveFrame(event):
        systemButton.config(image=systemButtonImg)

    systemButton = Label(winFrame,image=systemButtonImg,bg="black",cursor="hand2")
    systemButton.place(x=360,y=430)


    systemButton.bind('<Enter>',SystemButtonEnterFrame)
    systemButton.bind('<Enter>',SystemButtonLeaveFrame)

    #------------------- health button end-----------------------------#

    #-------------------account  button ----------------------------------#

    webButtonImg = PhotoImage(file="D:\\antivirus programs\\Bit-Link Antivirus Yt\\res\\Buttons\\Non-Hoved\\web.png")
    hovwebButtonImg = PhotoImage(file="D:\\antivirus programs\\Bit-Link Antivirus Yt\\res\\Buttons\\Hoved\\hovWeb.png")

    def WebButtonEnterFrame(event):
        webButton.config(image=hovwebButtonImg)

    def WebButtonLeaveFrame(event):
        webButton.config(image=webButtonImg)

    webButton = Label(winFrame,image=webButtonImg,bg="black",cursor="hand2")
    webButton.place(x=710,y=430)

    webButton.bind('<Enter>',WebButtonEnterFrame)
    webButton.bind('<Leave>',WebButtonLeaveFrame)

    #-------------------------Accounts Button End --------------------#

    # ----------------------Internet Button -------------------------#
    ToolsButtonImg = PhotoImage(file="D:\\antivirus programs\\Bit-Link Antivirus Yt\\res\\Buttons\\Non-Hoved\\tools.png" )
    hovToolsButtonImg = PhotoImage(file="D:\\antivirus programs\\Bit-Link Antivirus Yt\\res\\Buttons\\Hoved\\hovTools.png")

    def ToolsButtonEnterFrame(event):
        toolsButton.config(image=hovToolsButtonImg)

    def ToolsButtonLeaveFrame(event):
        toolsButton.config(image=ToolsButtonImg)

    toolsButton =Label(winFrame,image=ToolsButtonImg,bg="black",cursor="hand2")
    toolsButton.place(x=535, y=430)

    toolsButton.bind('<Enter>',ToolsButtonEnterFrame)
    toolsButton.bind('<Leave>',ToolsButtonLeaveFrame)

    #------------------------Internet Button End--------------------------#


    #------------------------footer    start------------------------------#
    global footerBannerImg
    footerBannerImg = PhotoImage(file="D:\\antivirus programs\\res\\footer.png")

    footerBanner = Label(winFrame,image=footerBannerImg,bg="white")
    footerBanner.place(x=170,y=605)

    #------------------------footer    End--------------------------------#

    #------------------------Logo frame start ------------------------#
    global logoLabelImg
    logoLabelImg = PhotoImage(file="D:\\antivirus programs\\BitLink\\Bit-Link Antivirus Pro Working\\res\\Logo\\logo.png").subsample(2,2)
    logoLabel = Label(winFrame,image =logoLabelImg,bg='gray17')
    logoLabel.place(x=10,y=0)

    global nameLabelImg
    nameLabelImg = PhotoImage(file="D:\antivirus programs\BitLink\Bit-Link Antivirus Pro Working\res\Logo\b logo.png").subsample(2,2)
    nameLabel = Label(winFrame,image=nameLabelImg,bg='grey17')
    nameLabel.place(x=90,y=20)

    #------------------------Logo frame end --------------------------#

    # #-----------------------Home button________________________#
    # global homeButtonImg
    #
    # homeButtonImg = PhotoImage(file="D:\\antivirus programs\\BitLink\\Bit-Link Antivirus Pro Working\\res\\Home Frame\\Current\\Home.png")
    #
    # homeButton = Label(winFrame,image=homeButtonImg,bg="gray17",cursor="hand2")
    # homeButton.place(x=155,y=570)
    #
    # #---------------------home button end-----------------------#

    # #--------------------Animation --- ----------------#

    global robotImg
    robotImg = PhotoImage(file= "D:\\antivirus programs\\BitLink\\Bit-Link Antivirus Pro Working\\res\\Home Frame\\Animation\\robotlink.png")

    robotAnimation = Label(winFrame, image=robotImg, bg="gray17")
    robotAnimation.place(x=405, y=150)

    global ani
    ani = 0

    def RobotAnimation():
        global ani

        if ani == 4:
            robotAnimation.place_configure(y=153)
            ani = 0

        elif ani == 2:
            robotAnimation.place_configure(y=150)

        ani += 1

        robotAnimation.after(200, RobotAnimation)

    RobotAnimation()

    # #--------------------Animation End ----------------#
    # #--------------------Sub-Frame --- ----------------#

    # #--------------------Proction-Frame --- ----------------#

    global protectionOn0Img

    protectionOn0Img = PhotoImage(file="res\\Home Frame\\Non-Hoved\\protection on0.png").subsample(2, 2)
    protectionOn0ImgHov = PhotoImage(file="res\\Home Frame\\Hoved\\protection on.png").subsample(2, 2)

    def ProtectionEnter(event):
        protectionOn0.config(image=protectionOn0ImgHov)

    def ProtectionLeave(event):
        protectionOn0.config(image=protectionOn0Img)

    protectionOn0 = Label(winFrame, image=protectionOn0Img, bg="gray17", cursor="hand2")
    protectionOn0.place(x=180, y=160)
    protectionOn0.bind('<Enter>', ProtectionEnter)
    protectionOn0.bind('<Leave>', ProtectionLeave)

    # #--------------------Proction-Frame End ----------------#

    # #--------------------Web-Frame --- ----------------#

    global webShieldImg

    webShieldImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\web sh.png").subsample(2, 2)
    webShieldImgHov = PhotoImage(file="res\\Home Frame\\Hoved\\web shield.png").subsample(2, 2)

    def WebShieldEnter(event):
        webShield.config(image=webShieldImgHov)

    def WebShieldLeave(event):
        webShield.config(image=webShieldImg)

    webShield = Label(winFrame, image=webShieldImg, bg="gray17", cursor="hand2")
    webShield.place(x=810, y=160)
    webShield.bind('<Enter>', WebShieldEnter)
    webShield.bind('<Leave>', WebShieldLeave)

    # #--------------------Web-Frame End ----------------#

    # #--------------------FireWall-Frame --- ----------------#

    global fireWallOnImg

    fireWallOnImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\fire wall on.png").subsample(2, 2)
    fireWallOnImgHov = PhotoImage(file="res\\Home Frame\\Hoved\\firewall.png").subsample(2, 2)

    def FireWallEnter(event):
        fireWallOn.config(image=fireWallOnImgHov)

    def FireWallLeave(event):
        fireWallOn.config(image=fireWallOnImg)

    fireWallOn = Label(winFrame, image=fireWallOnImg, bg="gray17", cursor="hand2")
    fireWallOn.place(x=160, y=220)

    fireWallOn.bind('<Enter>', FireWallEnter)
    fireWallOn.bind('<Leave>', FireWallLeave)

    # #--------------------FireWall-Frame End ----------------#

    # #--------------------FullScan-Frame --- ----------------#

    global fullScanImg

    fullScanImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\full scan.png").subsample(2, 2)
    fullScanImgHov = PhotoImage(file="res\\Home Frame\\Hoved\\full scan.png").subsample(2, 2)

    def FullScanEnter(e):
        fullScan.config(image=fullScanImgHov)

    def FullScanLeave(e):
        fullScan.config(image=fullScanImg)

    fullScan = Label(winFrame, image=fullScanImg, bg="gray17", cursor="hand2")
    fullScan.place(x=830, y=220)
    fullScan.bind('<Enter>', FullScanEnter)
    fullScan.bind('<Leave>', FullScanLeave)

    # #--------------------FullScan-Frame End ----------------#

    # #--------------------QuickScan-Frame --- ----------------#

    global quickScanImg

    quickScanImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\quick scan.png").subsample(2, 2)
    quickScanImgHov = PhotoImage(file="res\\Home Frame\\Hoved\\Quck Scan.png").subsample(2, 2)

    def QuickScanEnter(e):
        quickScan.config(image=quickScanImgHov)

    def QuickScanLeave(e):
        quickScan.config(image=quickScanImg)

    quickScan = Label(winFrame, image=quickScanImg, bg="gray17", cursor="hand2")
    quickScan.place(x=150, y=280)
    quickScan.bind('<Enter>', QuickScanEnter)
    quickScan.bind('<Leave>', QuickScanLeave)

    # #--------------------QuickScan-Frame End ----------------#
    # #--------------------RamBooster-Frame --- ----------------#

    global ramBoosterImg

    ramBoosterImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\ram boost.png").subsample(2, 2)
    ramBoosterImgHov = PhotoImage(file="res\\Home Frame\\Hoved\\ram boost.png").subsample(2, 2)

    def RamBoosterEnter(e):
        ramBooster.config(image=ramBoosterImgHov)

    def RamBoosterLeave(e):
        ramBooster.config(image=ramBoosterImg)

    ramBooster = Label(winFrame, image=ramBoosterImg, bg="gray17", cursor="hand2")
    ramBooster.place(x=840, y=280)
    ramBooster.bind('<Enter>', RamBoosterEnter)
    ramBooster.bind('<Leave>', RamBoosterLeave)

    # #--------------------RamBooster-Frame End ----------------#

    # #--------------------Smart Scan-Frame --- ----------------#

    global smartScanLblImg

    smartScanLblImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\smart scan.png").subsample(2, 2)
    smartScanLblImgHov = PhotoImage(file="res\\Home Frame\\Hoved\\smart scan.png").subsample(2, 2)

    def smartScanLblEnter(e):
        smartScanLbl.config(image=smartScanLblImgHov)

    def smartScanLblLeave(e):
        smartScanLbl.config(image=smartScanLblImg)

    smartScanLbl = Label(winFrame, image=smartScanLblImg, bg="gray17", cursor="hand2")
    smartScanLbl.place(x=160, y=340)
    smartScanLbl.bind('<Enter>', smartScanLblEnter)
    smartScanLbl.bind('<Leave>', smartScanLblLeave)

    # #--------------------Smart Scan-Frame End ----------------#

    # #--------------------Deep Scan-Frame --- ----------------#

    global deepScanImg

    deepScanImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\deep scan.png").subsample(2, 2)
    deepScanImgHov = PhotoImage(file='res\\Home Frame\\Hoved\\deep scan.png').subsample(2, 2)

    def DeepScanEnter(e):
        deepScan.config(image=deepScanImgHov)

    def DeepScanLeave(e):
        deepScan.config(image=deepScanImg)

    deepScan = Label(winFrame, image=deepScanImg, bg="gray17", cursor="hand2")
    deepScan.place(x=830, y=340)
    deepScan.bind("<Enter>", DeepScanEnter)
    deepScan.bind("<Leave>", DeepScanLeave)

    # #--------------------Deep Scan-Frame End ----------------#

    # #--------------------Help-Frame --- ----------------#

    global helpNsupportImg

    helpNsupportImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\help & support.png").subsample(2, 2)
    helpNsupportImgHov = PhotoImage(file="res\\Home Frame\\Hoved\\help.png").subsample(2, 2)

    def HelpEnter(e):
        helpNsupport.config(image=helpNsupportImgHov)

    def HelpLeave(e):
        helpNsupport.config(image=helpNsupportImg)

    helpNsupport = Label(winFrame, image=helpNsupportImg, bg="gray17", cursor="hand2")
    helpNsupport.place(x=180, y=400)
    helpNsupport.bind("<Enter>", HelpEnter)
    helpNsupport.bind("<Leave>", HelpLeave)

    # #--------------------Help-Frame End ----------------#

    # #--------------------Driver Update-Frame --- ----------------#

    global driverUpdateImg

    driverUpdateImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\driver update.png").subsample(2, 2)
    driverUpdateImgHov = PhotoImage(file="res\\Home Frame\\Hoved\\driver update.png").subsample(2, 2)

    def DriverUpdateEnter(e):
        driverUpdate.config(image=driverUpdateImgHov)

    def DriverUpdateLeave(e):
        driverUpdate.config(image=driverUpdateImg)

    driverUpdate = Label(winFrame, image=driverUpdateImg, bg="gray17", cursor="hand2")
    driverUpdate.place(x=810, y=400)
    driverUpdate.bind("<Enter>", DriverUpdateEnter)
    driverUpdate.bind("<Leave>", DriverUpdateLeave)

    # #--------------------Driver Update-Frame End ----------------#

    # #--------------------Sub-Frame End ----------------#

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################


def ScanFrame():
    # --------------------Global Var --------------------#
    global winFrame

    # --------------------Global Var End -----------------#

    winFrame.destroy()

    # --------------------Main Frame ---------------------#

    winFrame = Frame(window, width="1200", height="850", bg="gray17")
    winFrame.pack()
    winFrame.pack_propagate(0)

    # --------------------Main Frame End ------------------#

    # --------------------Footer Frame --------------------#

    global footerImg
    footerImg = PhotoImage(file='res\\footer.png')

    footerLabel = Label(winFrame, image=footerImg, bg="gray17")
    footerLabel.place(x=310, y=773)

    # --------------------Footer Frame End ----------------#

    # --------------------Logo Frame start --------------#

    global logoLabelImg
    logoLabelImg = PhotoImage(file='res\\Logo\\logo.png')
    logoLabel = Label(winFrame, image=logoLabelImg, bg='gray17')
    logoLabel.place(x=10, y=0)

    global nameLabelImg
    nameLabelImg = PhotoImage(file='res\\Logo\\b logo.png').subsample(2, 2)
    nameLabel = Label(winFrame, image=nameLabelImg, bg='gray17')
    nameLabel.place(x=90, y=20)
    # --------------------Logo Frame End ----------------#


    #--------------------Quick Scan-------------------------#

    global quickScanButton_1
    global quickScanButton_1_Hoved

    quickScanButton_1 = PhotoImage(file='res\\Scan Frame\\Non-Hoved\\Quick Scan.png').subsample(2, 2)
    quickScanButton_1_Hoved = PhotoImage(file='res\\Scan Frame\\Hoved\\Quick Scan.png').subsample(2, 2)

    def quickScanButton_1_Enter(e):
        quickScanButton_1place.config(image=quickScanButton_1_Hoved)

    def quickScanButton_1_Leave(e):
        quickScanButton_1place.config(image=quickScanButton_1)

    quickScanButton_1place = Label(winFrame, image=quickScanButton_1, bg='gray17', cursor="hand2")
    quickScanButton_1place.place(x=530, y=100)

    quickScanButton_1place.bind('<Enter>', quickScanButton_1_Enter)
    quickScanButton_1place.bind('<Leave>', quickScanButton_1_Leave)

    # --------------------Quick_Scan End ----------------#

    # --------------------Smart_Scan --------------------#

    global smartScanButton_1
    global smartScanButton_1_Hoved

    smartScanButton_1 = PhotoImage(file='res\\Scan Frame\\Non-Hoved\\smart Scan.png').subsample(2, 2)
    smartScanButton_1_Hoved = PhotoImage(file='res\\Scan Frame\\Hoved\\smart Scan.png').subsample(2, 2)

    def smartScanButton_1_Enter(e):
        smartScanButton_1place.config(image=smartScanButton_1_Hoved)

    def smartScanButton_1_Leave(e):
        smartScanButton_1place.config(image=smartScanButton_1)

    smartScanButton_1place = Label(winFrame, image=smartScanButton_1, bg='gray17', cursor="hand2")
    smartScanButton_1place.place(x=510, y=170)

    smartScanButton_1place.bind('<Enter>', smartScanButton_1_Enter)
    smartScanButton_1place.bind('<Leave>', smartScanButton_1_Leave)

    # --------------------Smart_Scan End ----------------#

    # --------------------Full_Scan --------------------#

    global fullScanButton_1
    global fullScanButton_1_Hoved

    fullScanButton_1 = PhotoImage(file='res\\Scan Frame\\Non-Hoved\\Full Scan.png').subsample(2, 2)
    fullScanButton_1_Hoved = PhotoImage(file='res\\Scan Frame\\Hoved\\Full Scan.png').subsample(2, 2)

    def fullScanButton_1_Enter(e):
        fullScanButton_1place.config(image=fullScanButton_1_Hoved)

    def fullScanButton_1_Leave(e):
        fullScanButton_1place.config(image=fullScanButton_1)

    fullScanButton_1place = Label(winFrame, image=fullScanButton_1, bg='gray17', cursor="hand2")
    fullScanButton_1place.place(x=510, y=240)

    fullScanButton_1place.bind('<Enter>', fullScanButton_1_Enter)
    fullScanButton_1place.bind('<Leave>', fullScanButton_1_Leave)

    # --------------------Full_Scan End ----------------#

    # --------------------Deep_Scan --------------------#

    global deepScanButton_1
    global deepScanButton_1_Hoved

    deepScanButton_1 = PhotoImage(file='res\\Scan Frame\\Non-Hoved\\Deep Scan.png').subsample(2, 2)
    deepScanButton_1_Hoved = PhotoImage(file='res\\Scan Frame\\Hoved\\Deep Scan.png').subsample(2, 2)

    def deepScanButton_1_Enter(e):
        deepScanButton_1place.config(image=deepScanButton_1_Hoved)

    def deepScanButton_1_Leave(e):
        deepScanButton_1place.config(image=deepScanButton_1)

    deepScanButton_1place = Label(winFrame, image=deepScanButton_1, bg='gray17', cursor="hand2")
    deepScanButton_1place.place(x=510, y=310)

    deepScanButton_1place.bind('<Enter>', deepScanButton_1_Enter)
    deepScanButton_1place.bind('<Leave>', deepScanButton_1_Leave)

    # --------------------Deep_Scan End ----------------#

    # --------------------Custom_Scan --------------------#

    global CustomScanButton_1
    global CustomScanButton_1_Hoved

    CustomScanButton_1 = PhotoImage(file='res\\Scan Frame\\Non-Hoved\\Custom Scan.png').subsample(2, 2)
    CustomScanButton_1_Hoved = PhotoImage(file='res\\Scan Frame\\Hoved\\Custom Scan.png').subsample(2, 2)

    def CustomScanButton_1_Enter(e):
        CustomScanButton_1place.config(image=CustomScanButton_1_Hoved)

    def CustomScanButton_1_Leave(e):
        CustomScanButton_1place.config(image=CustomScanButton_1)

    CustomScanButton_1place = Label(winFrame, image=CustomScanButton_1, bg='gray17', cursor="hand2")
    CustomScanButton_1place.place(x=530, y=380)

    CustomScanButton_1place.bind('<Enter>', CustomScanButton_1_Enter)
    CustomScanButton_1place.bind('<Leave>', CustomScanButton_1_Leave)

    # --------------------Custom_Scan End ----------------#

    # --------------------Main Logo ----------------------#

    global scanFrameMainLogo
    global scanFrameMainLogoHoved
    scanFrameMainLogo = PhotoImage(file='res\\Scan Frame\\main logo.png')
    scanFrameMainLogoHoved = PhotoImage(file='res\\Scan Frame\\main logo hoved.png')

    def scanFrameMainLogoEnter(event):
        scanFrameMainLogoPlace.config(image=scanFrameMainLogoHoved)

    def scanFrameMainLogoLeave(event):
        scanFrameMainLogoPlace.config(image=scanFrameMainLogo)

    scanFrameMainLogoPlace = Label(winFrame, image=scanFrameMainLogo, bg='gray17', cursor="hand2")
    scanFrameMainLogoPlace.place(x=772, y=100)

    scanFrameMainLogoPlace.bind('<Enter>', scanFrameMainLogoEnter)
    scanFrameMainLogoPlace.bind('<Leave>', scanFrameMainLogoLeave)

    # --------------------Main Logo End-------------------#




HomeviewDarkTheme()

window.mainloop()


#end of gui ##########################################
