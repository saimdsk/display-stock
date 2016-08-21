import runAnalytics
from tkinter import *
import os
import centerWindow

#Creates the application and gives it a title and set dimensions
loadApplication = Tk()
loadApplication.title("Stock Analytics")
loadApplication.geometry("1080x720")

#Creates the label and input widget
label1 = Label(loadApplication, text = "Ticker")
input1 = Entry(loadApplication)

#Button to execture the run command in runAnalytics
loadAnalytics = Button(loadApplication, text = "Load Analytics", command=lambda: runAnalytics.run(input1))

#Runs the center window command to center the application on the screen
centerWindow.center(loadApplication)

#Packs the widgets into the application
label1.pack()
input1.pack()
loadAnalytics.pack()

#Starts the main loop wich everything should be initialized before
#Execution of tkinter application does not work after mainloop
loadApplication.mainloop()
