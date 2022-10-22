# Xialu Zou
# HW2
import yfinance as yf
import datetime
from flask import Flask,render_template,request,redirect

app = Flask(__name__)
@app.route('/',methods = ['POST' , 'GET'])

def index():
    return render_template("stock.html")

@app.route('/show',methods = ['POST','GET'])
def show():
    try:
        symbol = request.args.get('symbol')
        print(symbol)
        # using now() to get current time
        current_time = datetime.datetime.now()
        weekday = current_time.strftime('%A')
        stock_info = yf.Ticker(symbol).info
        market_price = stock_info['regularMarketPrice']
        if (market_price == None):
            return render_template('stock.html',msg = "Wrong symbol, Please enter again")
        name = stock_info['shortName']
        previous = float(stock_info['previousClose'])
        valueChange = float(market_price - previous)
        percentChange = valueChange * 100 / previous
        s1 = str(market_price) + " "
        if (valueChange >= 0):
            s1 = s1 + "+" + str(round(abs(valueChange), 2))
        else:
            s1 = s1 + "-" + str(round(abs(valueChange), 2))

        if (percentChange < 0):
            s1 = s1 + "(-%" + str(round(abs(percentChange), 2)) + ")"
        else:
            s1 = s1 + "(+%" + str(round(abs(percentChange), 2)) + ")"

        return symbol+" "+str(weekday)+" "+str(current_time)+" "+name+" "+s1
    except Exception as e:
        print(e)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

