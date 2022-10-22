# Xialu Zou
# HW2
import yfinance as yf
import datetime
import traceback
import sys


def main():
    # using now() to get current time
    current_time = datetime.datetime.now()
    weekday = current_time.strftime('%A')

    while True:
        try:
            symbol = input("Please enter the stock Symbol: ")
            stock_info = yf.Ticker(symbol).info
            market_price = stock_info['regularMarketPrice']
            if(market_price==None):
                print("Wrong Input Symbol")
                continue
            name = stock_info['shortName']


            previous = float(stock_info['previousClose'])
            valueChange = float(market_price - previous)
            percentChange = valueChange*100/previous
            print(symbol)
            print(weekday,current_time)
            print(name+"("+symbol+")")
            s1=str(market_price)+" "
            if(valueChange>=0):
                s1=s1+"+" + str(round(abs(valueChange),2))
            else:
                 s1=s1+"-" + str(round(abs(valueChange),2))

            if(percentChange<0):
                s1=s1+"(-%" + str(round(abs(percentChange),2))+")"
            else:
                s1 = s1 + "(+%" + str(round(abs(percentChange),2)) + ")"
                print(s1)
        except Exception as e: print(e)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

