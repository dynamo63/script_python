##################
#--Author:Sabil--#
##################

#!usr/bin/python3
#coding:utf-8

from PyQt5.QtWidgets import *
import sys


#Notre classe herite de la classe mere des fenetre!...QMa...
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow,self).__init__()
        self.initUI()

    def initUI(self):
        """Initialisation of user interface"""
        self.setGeometry(100,50,300,250)
        self.setWindowTitle("Ma fenetre Qt")

        #Nos widgets
        message=QLabel("Hello World",self)
        message.move(100,50)
        self.bouton=QPushButton("Cliquez",self)
        self.bouton.move(80,30)
        self.bouton.clicked.connect(self.warning)

        #--------On cree un menu---------
        ObjectMain=self.menuBar()

        ObjectOption=ObjectMain.addMenu("Option")
        OptionQuit=QAction("Quitter",self)
        OptionQuit.setShortcut("Ctrl+Q")
        ObjectOption.addAction(OptionQuit)

        OptionQuit.triggered.connect(self.closed)

    def closed(self):
        quit()

    def warning(self):  
        global i
        i+=1
        QMessageBox.about(self,"Message","Ca fait {} fois".format(i) )

if __name__=='__main__':
    i=0
    app=QApplication(sys.argv)
    fenetre=MainWindow()
    fenetre.show()
    app.exec_()
