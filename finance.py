
import yfinance as yf

USDRUB = yf.Ticker("RUB=X")
usd_rub = USDRUB.info['ask']
Tesla = yf.Ticker("TSLA")
tsla =  Tesla.info['ask']
Apple = yf.Ticker("AAPL")
apple =  Apple.info['ask']
