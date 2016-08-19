from yahoo_finance import Share
import tkinter
import os
import centerWindow


def run(input1):

    ticker = Share(input1.get())
    print(type(ticker))
    loadAnalytics = tkinter.Tk()
    loadAnalytics.title("$ + ticker +  Data")
    loadAnalytics.geometry("1080x720")

    print ("Price per share: " + ticker.get_price())

    ticker.refresh()
    print ("Price per share: " + ticker.get_price())

    print("The dividend yield is: " + ticker.get_dividend_yield())

    print("The 52 week low is: " + ticker.get_year_low())
    print("The 52 week high is: " + ticker.get_year_high())
    print("The volume is: " + ticker.get_volume())

    print("The previous close was: " + ticker.get_prev_close())
    print("The previous open was: " + ticker.get_open())

    loadAnalytics.mainloop()
