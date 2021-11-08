from flask import Flask
from binance_connect_Final import SIGNALS_BY_SYMBOL
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
import time

app = Flask(__name__)

executors = {
    "default": ThreadPoolExecutor(16), 
    "processpool": ProcessPoolExecutor(4)
}

def job():

    print("CHECKING FOR SIGNALS ...")

    coin_list = ["SHIBUSDA", "MANAUSDT" ,"UNIUSDT", "GALAUSDT"]
    for coin in coin_list:
        SIGNALS_BY_SYMBOL(symbols=coin)


sched = BackgroundScheduler(timezone='Asia/Singapore', executors=executors)

@app.route('/')
def hello_world():
    return "HEllo World!"


@app.route("/<pairname>")
def pair_signals(pairname):
    return f"This is {pairname} buying signals"

if  __name__ == '__main__':
    input("PRESS ENTER TO RUN")
    while True :
        print("### SCANING NOW ###")
        job()
        time.sleep(60)
        print("######"*10)

    print("END..")