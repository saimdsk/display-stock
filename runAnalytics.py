from yahoo_finance import Share
from tkinter import *
import os
import centerWindow

#GLoval variables that will be used in algorithm.py
global risk
global moving_average

#Function that is called in main.py to start the new application, keeping loadApplication running
#Inherts input1 from main.py
def run(input1):
    #Creates the application and gives it a title and set dimensions
    ticker = Share(input1.get())
    loadAnalytics = Tk()
    loadAnalytics.title("Stock Analytics")
    loadAnalytics.geometry("800x450")

    #Centers the application on the screen
    centerWindow.center(loadAnalytics)

    #Refreshes all stock data
    ticker.refresh()

    #Custom functions using the built in yahoo-finance functions as variables
    #If an equation uses a dividend, put it inside the else statement, NOT HERE (Program will not execute)
    previous_gain          = format(float(ticker.get_price()) - float(ticker.get_open()), '.2f')
    previous_gain_percent  = format((float((previous_gain))/float((ticker.get_price())))*100, '.2f')
    risk                   = format((float(ticker.get_price())-float(ticker.get_year_low()))/(float(ticker.get_year_high()))*100, '.2f')
    moving_average_percent = format((float(ticker.get_50day_moving_avg())/float(ticker.get_200day_moving_avg()))*100, '.2f')
    moving_average = format((float(ticker.get_50day_moving_avg())/float(ticker.get_200day_moving_avg())), '.2f')

    #Creates the label widgets to output stock data
    share_price            = Label(loadAnalytics,text='Share Price: {}'.format(ticker.get_price())).pack(fill=X)
    output_gain            = Label(loadAnalytics,text='Previous Market Change: ${}'.format(str(previous_gain))).pack(fill=X)
    output_gain_percentage = Label(loadAnalytics,text='Previous Market Percentage Change: {}%'.format(str(previous_gain_percent))).pack(fill=X)
    prev_open              = Label(loadAnalytics,text='Previous Open: {}'.format(ticker.get_open())).pack(fill=X)
    dividend_yield         = Label(loadAnalytics,text='Dividend Yield: {}'.format(ticker.get_dividend_yield())).pack(fill=X)
    year_low               = Label(loadAnalytics,text='52 Week Low: {}'.format(ticker.get_year_low())).pack(fill=X)
    year_high              = Label(loadAnalytics,text='52 Week High: {}'.format(ticker.get_year_high())).pack(fill=X)
    volume                 = Label(loadAnalytics,text='Volume: {}'.format(ticker.get_volume())).pack(fill=X)
    market_cap             = Label(loadAnalytics,text='Market Cap: {}'.format(ticker.get_market_cap())).pack(fill=X)
    fifty_move             = Label(loadAnalytics,text='50 Day Moving Average: ${}'.format(ticker.get_50day_moving_avg())).pack(fill=X)
    hundred_move           = Label(loadAnalytics,text='200 Day Moving Average ${}'.format(ticker.get_200day_moving_avg())).pack(fill=X)
    ebitda                 = Label(loadAnalytics,text="EBITDA: {}".format(ticker.get_ebitda())).pack(fill=X)
    pb_ratio               = Label(loadAnalytics,text="P/B Ratio: {}".format(ticker.get_price_book())).pack(fill=X)
    estimated_risk         = Label(loadAnalytics,text='Expected Risk at Current Price: {}%'.format(str(risk))).pack(fill=X)
    moving_avg_percent = Label(loadAnalytics,text='50 Day Move to 200 Day Move Ratio: {}%'.format(str(moving_average_percent))).pack(fill=X)
    #Solves the issue where if a stock has no dividend, the program would crash
    #This work around makes it so different a output is used if no dividend is present
    if ticker.get_dividend_yield() is not None:
        dividend_share           = format((float(ticker.get_price())*float(ticker.get_dividend_yield()))/100, '.2f')
        dividend_per_share     = Label(loadAnalytics,text='Dividend Per Share: {}$'.format(str(dividend_share))).pack(fill=X)

    #Mainloop for loadAnalytics, must keep all widgets within the mainloop
    #Execution of tkinter application does not work after mainloop
    loadAnalytics.mainloop()
