import runAnalytics
import tkinter
import os
import centerWindow

#def test_func(val):
#print(val)

loadApplication = tkinter.Tk()
loadApplication.title("Stock Analytics")
loadApplication.geometry("1080x720")

label1 = tkinter.Label(loadApplication, text = "Ticker")
input1 = tkinter.Entry(loadApplication)

loadAnalytics = tkinter.Button(loadApplication, text = "Load Analytics", command=lambda: runAnalytics.run(input1))

centerWindow.center(loadApplication)

loadAnalytics.pack()
label1.pack()
input1.pack()

loadApplication.mainloop()
