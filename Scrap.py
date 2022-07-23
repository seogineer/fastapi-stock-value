from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override()


class Scrap:
    def get_stock(ticker: str, start: str, end: str):
        datas = pdr.get_data_yahoo(ticker, start, end)
        return {"result":datas["Adj Close"]}
