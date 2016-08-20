import runAnalytics
from tkinter import *
import os
import centerWindow

loadApplication = Tk()
loadApplication.title("Stock Analytics")
loadApplication.geometry("1080x720")

label1 = Label(loadApplication, text = "Ticker")
input1 = Entry(loadApplication)

loadAnalytics = Button(loadApplication, text = "Load Analytics", command=lambda: runAnalytics.run(input1))

centerWindow.center(loadApplication)


label1.pack()
input1.pack()
loadAnalytics.pack()

loadApplication.mainloop()
