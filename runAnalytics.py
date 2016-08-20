from yahoo_finance import Share
from tkinter import *
import os
import centerWindow

def run(input1):
    ticker = Share(input1.get())
    loadAnalytics = Tk()
    loadAnalytics.title("Stock Analytics")
    loadAnalytics.geometry("1080x720")
    centerWindow.center(loadAnalytics)

    ticker.refresh()

    share_price    = Label(loadAnalytics,text='Share Price: {}'.format(ticker.get_price())).pack()
    prev_open      = Label(loadAnalytics,text='Previous Open: {}'.format(ticker.get_open())).pack()
    prev_close     = Label(loadAnalytics,text='Previous CLose: {}'.format(ticker.get_prev_close())).pack()
    dividend_yield = Label(loadAnalytics,text='Dividend Yield: {}'.format(ticker.get_dividend_yield())).pack()
    year_low       = Label(loadAnalytics,text='52 Week Low: {}'.format(ticker.get_year_low())).pack()
    year_high      = Label(loadAnalytics,text='52 Week High: {}'.format(ticker.get_year_high())).pack()
    volume         = Label(loadAnalytics,text='Volume: {}'.format(ticker.get_volume())).pack()

    previous_gain            = format(float(ticker.get_open()) - float(ticker.get_prev_close()), '.2f')
    previous_gain_percentage = format((float((previous_gain))/float((ticker.get_prev_close())))*100, '.2f')

    output_gain            = Label(loadAnalytics,text='Previous Market Change: ${}'.format(str(previous_gain))).pack()
    output_gain_percentage = Label(loadAnalytics,text='Previous Market Percentage Change: {}%'.format(str(previous_gain_percentage))).pack()

    loadAnalytics.mainloop()
