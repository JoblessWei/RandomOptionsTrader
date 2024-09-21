import time
import Trader
import Keys
from Trader import *
from pathlib import Path
from Get_Ticker import tickers
from alpaca.trading.client import TradingClient
from alpaca.trading.enums import OrderSide, TimeInForce, QueryOrderStatus
from alpaca.trading.requests import LimitOrderRequest, MarketOrderRequest

trading_client = TradingClient(Keys.alpaca_api_key ,Keys.alpaca_secret_key )

def buyOrder(optionName):
    market_order_data = MarketOrderRequest(
    symbol = optionName,
    qty = '1',
    side = OrderSide.BUY,
    time_in_force = TimeInForce.DAY,
)
    order = trading_client.submit_order(market_order_data)
   
# print(f"You have (randomly) bought a {sym} {x} @ {Strike} for ${avg:.2f} (Total:${avg * 100:.2f}) per share expiring {expiryDate}")

def sellOrder(optionName):
    market_order_data = MarketOrderRequest(
        symbol = optionName,
        qty = '1',
        side = OrderSide.SELL,
        time_in_force = TimeInForce.DAY,
)
    order = trading_client.submit_order(market_order_data)


def buyOption():
    SYMBOL = getRandTicker(tickers)
    callsOrPuts = getCallorPuts()
    stock = yf.Ticker(SYMBOL)
    expiryDate = stock.options[0]
    getOptChain(SYMBOL,callsOrPuts) # Populates the above lists
    randOPT = getRandOption(options) # Selects random option from list of options
    print(options,avgPrice,strikePrice)
    print(randOPT)
    optName = options[randOPT]
    Strike = strikePrice[randOPT]
    avg = avgPrice[randOPT]
    print(optName,  Strike)

    try:
        buyOrder(optName)
        print(f"You have (randomly) bought a {SYMBOL} @ {Strike} for ${avg:.2f}  per share (Total:${avg * 100:.2f}) expiring {expiryDate}")
    except Exception as e:
        print(e)
        print('Insufficient Buying Power')
    
    clearLists(options, strikePrice, avgPrice)


while True:
    buyOption()
    time.sleep(10)
