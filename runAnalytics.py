from yahoo_finance import Share
from tkinter import *
import os
import centerWindow

#Function that is called in main.py to start the new application, keeping loadApplication running
#Inherts input1 from main.py
def run(input1):
    #Creates the application and gives it a title and set dimensions
    ticker = Share(input1.get())
    loadAnalytics = Tk()
    loadAnalytics.title("Stock Analytics")
    loadAnalytics.geometry("1080x720")

    #Centers the application on the screen
    centerWindow.center(loadAnalytics)

    #Refreshes all stock data
    ticker.refresh()

    #Creates the label widgets to output stock data
    share_price    = Label(loadAnalytics,text='Share Price: {}'.format(ticker.get_price())).pack()
    prev_open      = Label(loadAnalytics,text='Previous Open: {}'.format(ticker.get_open())).pack()
    dividend_yield = Label(loadAnalytics,text='Dividend Yield: {}'.format(ticker.get_dividend_yield())).pack()
    year_low       = Label(loadAnalytics,text='52 Week Low: {}'.format(ticker.get_year_low())).pack()
    year_high      = Label(loadAnalytics,text='52 Week High: {}'.format(ticker.get_year_high())).pack()
    volume         = Label(loadAnalytics,text='Volume: {}'.format(ticker.get_volume())).pack()
    market_cap     = Label(loadAnalytics,text='Market Cap: {}'.format(ticker.get_market_cap())).pack()

    #Custom functions which uses the yahoo-finance functions to create new ones
    previous_gain            = format(float(ticker.get_price()) - float(ticker.get_open()), '.2f')
    previous_gain_percentage = format((float((previous_gain))/float((ticker.get_price())))*100, '.2f')
    dividend_share           = format((float(ticker.get_price())*float(ticker.get_dividend_yield()))/100, '.2f')
    risk                     = format((float(ticker.get_price))-float(ticker.get_year_low()))/(float(ticker.get_year_high)))

    #Creeats the widgets to output the results of the above functions
    output_gain            = Label(loadAnalytics,text='Previous Market Change: ${}'.format(str(previous_gain))).pack()
    output_gain_percentage = Label(loadAnalytics,text='Previous Market Percentage Change: {}%'.format(str(previous_gain_percentage))).pack()
    dividend_per_share     = Label(loadAnalytics,text='Dividend Per Share: {}$'.format(str(dividend_share))).pack()
    estimated_risk         = Label(loadAnalytics,text='Expected Risk at Current Price{}%'.format(str(risk))).pack()

    #Maiinloop for loadAnalytics, must keep all widgets within the mainloop
    loadAnalytics.mainloop()
