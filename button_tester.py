#!/usr/bin/env python3
# importing libraries
# source link for errors: https://stackoverflow.com/questions/56451682/pyqt5-and-anaconda-modulenotfounderror-no-module-named-pyqt5
# basic push_button code: https://www.geeksforgeeks.org/pyqt5-how-to-create-and-get-the-name-of-push-button/
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import rospy
from std_srvs.srv import Trigger, TriggerResponse



class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        mainLayout = QGridLayout()

        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(600, 600, 600, 600)
        self.client = rospy.ServiceProxy("ButtonService",Trigger) #creating client in init. class, use this to send something to service

        self.ButtonTwo()
        self.UiComponents()

        self.show()






    def UiComponents(self):
        # creating a push button
        self.button = QPushButton("Big Red Button", self)
        self.button.setStyleSheet("background-color : red")
        self.setStyleSheet("background-color: grey;")

        # setting geometry of button
        self.button.setGeometry(200, 200, 200, 200)
        self.button.move(300, 100)

        # setting name
        # button.setAccessibleName("don't press the button")
        # adding action to a button
        self.button.clicked.connect(self.clickme)
#clickme is alike to the callback functions in server/client nodes.
#tells ROS what to do after button is pressed.

    def ButtonTwo(self):#just a function so its ok to have another function defining a diff button. (i think)
        self.button = QPushButton("Small Blue Button", self)
        self.button.setStyleSheet("background-color : blue")
        self.setStyleSheet("background-color: black;")

        # setting geometry of button
        self.button.setGeometry(200, 200, 200, 200)
        self.button.move(10,100)

        # setting name
        # button.setAccessibleName("don't press the button")
        # adding action to a button
        self.button.clicked.connect(self.clickme)

    def ButtonThree(self):
        self.button =

    def clickme(self):
        res = self.client() #calling client
        if res.success == True:
            print(1)
        #ROS_PROGRAM = QProcess(self)
        #print(1) test case

        
if __name__ == '__main__':
    rospy.init_node("button_GUI_node")  # init node, creating the node to communicate with other nodes.
    rospy.wait_for_service("ButtonService")
    app = QApplication(sys.argv)
    mainLauncher =  Window() #general GUI config. (where all gui is)
    mainLauncher.show() #showing GUI
    sys.exit(app.exec_())

