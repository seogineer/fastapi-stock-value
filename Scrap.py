import yfinance as yf


class Scrap:
    def get_stock(ticker: str, start: str, end: str):
        datas = yf.download(ticker, start, end)
        return {"result":datas["Adj Close"]}