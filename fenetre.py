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
        self.CentralWidget=QWidget(self)
        self.setCentralWidget(self.CentralWidget)
        self.initUI()

    def initUI(self):
        """Initialisation of user interface"""
        self.setGeometry(100,50,300,250)
        self.setWindowTitle("Ma fenetre Qt")

        #Nos widgets
        message=QLabel("Hello World",self.CentralWidget)
        bouton=QPushButton("Cliquez",self.CentralWidget)
        bouton.clicked.connect(self.warning)

        #Positionnement....
        h_box=QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(message)
        h_box.addStretch()

        v_box=QVBoxLayout()
        v_box.addStretch()
        v_box.addWidget(bouton)
        v_box.addStretch()

        v_box.addLayout(h_box)

        self.CentralWidget.setLayout(v_box)
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
