import threading
from pytube import YouTube
import pytube
import sys
from PyQt5 import QtWidgets, QtGui, QtCore

#Defining A Main Function 
def main():

    #Creating an App Object
    app=QtWidgets.QApplication(sys.argv)

    #Creating A Window
    win=QtWidgets.QWidget()

    #Setting Window Title
    win.setWindowTitle('YouTube Video Downloader')

    #Setting The Window Geometry
    win.setGeometry(400,130,500,500)

    #Creating A Pallete to Color To set Background Color Of Window 
    p=win.palette()
    p.setColor(win.backgroundRole(),QtCore.Qt.black)
    win.setPalette(p)

    #Heading Label
    head=QtWidgets.QLabel(win)
    head.setText("YouTube Video Downloader")
    head.move(0,0)
    head.setFixedWidth(500)
    head.setAlignment(QtCore.Qt.AlignCenter)
    head.setFont(QtGui.QFont("Arial",20))
    head.setStyleSheet("background-color : orange; color : #fff; font-weight : bold;")

    #Label For Video Link
    vid_link=QtWidgets.QLabel(win)
    vid_link.setText("Video Link")
    vid_link.move(45,140)
    vid_link.setFont(QtGui.QFont("Arial",20))
    vid_link.setStyleSheet("color : orange;")

    #Entry Widget To Enter Video Link
    ent=QtWidgets.QLineEdit(win)
    ent.move(200,140)
    ent.setFixedWidth(250)
    ent.setFont(QtGui.QFont("Arial",20))
    ent.setStyleSheet("background-color : #000; color : orange; border : 1px solid orange;")

    #Function To binded To Download Button
    def fun():
        fun1()

    #Button For Downloading
    btn=QtWidgets.QPushButton(win)
    btn.setText("Download")
    btn.setStyleSheet("background-color : #000; color : orange; border : 1px solid orange;")
    btn.move(120,280)
    btn.setFont(QtGui.QFont("Arial",20))
    btn.setFixedWidth(300)
    btn.setFixedHeight(50)
    btn.clicked.connect(fun)

    #Progress Bar For Downloading Status
    pbar=QtWidgets.QProgressBar(win)
    pbar.setValue(10)
    pbar.move(-1000,0)
    pbar.setFixedWidth(350)

    #Label For Showing The Percentage Of Download Completed
    down_perc=QtWidgets.QLabel(win)
    down_perc.setText("0%")
    down_perc.move(-1000,190)
    down_perc.setFixedWidth(200)
    down_perc.setFont(QtGui.QFont("Arial",30))
    down_perc.setStyleSheet("color : orange;")

    #Function Caller For Downloading
    def fun2():
        fun3()

    #Function For Checking The User Input
    def fun1():
        a=str(ent.text())
        if not a:
           QtWidgets.QMessageBox.warning(win,"YouTube Video Downloader","Please Enter The Video Link!",QtWidgets.QMessageBox.Ok)
        else:
           vid_link.move(-1000,0)
           ent.move(-1000,0)
           btn.move(-1000,0)
           pbar.move(100,250)
           down_perc.move(245,190)

           #Calling The Downloading Function After 4 Seconds
           QtCore.QTimer.singleShot(4000,fun2)

    #Function For Downloading
    def fun3():
        SAVE_PATH="C:/Users/admin/Downloads"
        link=str(ent.text())

        global size
        size=0

        global point
        point=0

        #Function For Updating The ProgressBar And Download Label
        def fun4():
            fun5()

        #Bytes And Percentage Calculating Function
        def fun(a,b,c):
            tr=threading.Thread(target=fun4)
            tr.start()
            global size
            global point
            if size==0:
               size=int(str(c).strip())
            cur_size=int(str(c).strip())
            null=int(size-cur_size)
            perc=(null/size)*100

            #Uncomment This To Display The Downloading Status on IDLE or for Printing It.
##            if perc==100.0:
##               print(f'{str(perc)[:3]}%')
##            else:
##               print(f'{str(perc)[:4]}%')

            point=int(perc)
            if point==100:
               win.destroy()

        #Function To Update ProgressBar And Label
        def fun5():
            pbar.setValue(int(point+2))
            down_perc.setText(f"{int(point+2)}%")
            down_perc.move(235,190)

        #Connecting The Link
        try:
          yt=pytube.YouTube(link,on_progress_callback=fun)
        except:
          print("Connection Error")
        stream=yt.streams.first()
        stream.download(SAVE_PATH)

        print("done")
        print(size)

    #Displays The Window
    win.show()

    #Exits The App
    sys.exit(app.exec_())

#Calling The MAin Function To Run The Code
main()
