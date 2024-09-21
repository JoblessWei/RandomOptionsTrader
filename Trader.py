# Use Alpaca API to paper trade on site
from alpaca.trading.client import TradingClient
from alpaca.trading.enums import OrderSide, TimeInForce, QueryOrderStatus
from alpaca.trading.requests import LimitOrderRequest, MarketOrderRequest
import yfinance as yf   
import pandas as pd
from Get_Ticker import tickers
import Keys
import random

def getRandTicker(ticks):
    """
    Params:
    tickers: a list 

    Returns:
    Symbol, an element from that list
    """
    SYMBOL = random.choice(ticks)
    return SYMBOL


def getCallorPuts():
    calls = random.choice([0,1]) # Flip a coin and choose puts if it "lands on tails"
    return calls

options = []
strikePrice = []
avgPrice = []
# Find the 3 in the money and 3 out of the money options
def getOptChain(symbol,cORp): #Populate the global lists: options, strikePrice, and avgPrice
    global options,strikePrice,avgPrice
    ITM = not cORp
    stock = yf.Ticker(symbol)
    expiryDate = stock.options[0]
    optchain = stock.option_chain(expiryDate) #Gets all options chains for symbol that expire in the next week
    # print(optchain)
    if cORp: 
        df = optchain.calls # Opens the data frame for options chain of specific stock
    else:
        df = optchain.puts
    
    first = 0
    for index, row in df.iterrows():
        if row['inTheMoney'] == ITM: # Find the first OTM option for calls or puts
            first = index
            break

    max = first + 2 # To include the other 2 OTM options
    first -= 3 # We want to include the first 3 ITM options nearest to price of stock

    if first < 0 or max > len(df.index): #Checks if going forward or backwards ends up out of the table
        first = 0
        max = len(df.index) - 1
        
    for index, row in df.iterrows(): #iterates through each row of data frame
        if index == first and first <= max:
            options.append(row['contractSymbol']) # Add the data we need to their respective lists
            strikePrice.append(row['strike']) 
            avgPrice.append((row['bid'] + row['ask'] / 2))
            first += 1

def getRandOption(opts):
    return random.randrange(len(opts)) # Picks a random option from options list

def clearLists(opts,strikes,avgs):
    opts.clear()
    strikes.clear()
    avgs.clear()