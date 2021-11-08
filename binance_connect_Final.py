from binance.client import Client
from binance.enums import KLINE_INTERVAL_1MINUTE
from binance.enums import *
import matplotlib.pyplot as plt
import talib
import numpy as np
from songline import Sendline


token = "rsu6MSWeYH6W8RNOV09K2yh4rQjac6kSkEczQcl18H5"
messenger = Sendline(token)


API_KEY = "byXBIG4SDebx65km6QFuxzkMLep0XM45Puhz02cwLNL80eit3ecXe0dh5pCIVyA2"
SECRET_KEY = "YXVrEKoFvhnu8kGJXEu0laILD2EWZYQMS8AH0QzfqFQRDe06eBhGiUZi7up19Xc3"
client = Client(API_KEY, SECRET_KEY)


def SIGNALS_BY_SYMBOL(symbols):

    klines = client.get_historical_klines("MANAUSDT", Client.KLINE_INTERVAL_1MINUTE, "4 minutes ago UTC")

    closes = [float(i[4]) for i in klines]
    closes = np.array(closes)

    ema12 = talib.EMA(closes, timeperiod=12)
    ema26 = talib.EMA(closes, timeperiod=26)
    
    crossover = [] 
    crossunder = [] 

    for idx, val in enumerate(zip(ema12, ema26)):
        i = val[0]
        j = val[1]

        if (ema12[idx-1] < ema26[idx-1] and (i > j)) :
            print("BULLISH HERE")
            crossover.append(i) 
            messenger.sendtext(f'{symbols} CAN BULLISH HERE ▲▲▲ BUY ▲▲▲')

        elif (ema12[idx-1] > ema26[idx-1] and (i < j)) : 
            print("BEARISH HERE")
            crossunder.append(i)
            messenger.sendtext(f'{symbols} CAN BEARISH HERE ▼▼▼ SELL ▼▼▼')

        else:
            crossover.append(None)
            crossunder.append(None)
            print("NO SIGNAL FOR {}".format(symbols))

    crossover = np.array(crossover)
    crossunder = np.array(crossunder)
    