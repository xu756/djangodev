from datetime import datetime

import yfinance as yf


# 获取公司的股票价格数据
def get_stock_prices(company_name, years=3):
    # 设置数据获取的结束和开始时间
    end = datetime.now()
    start = datetime(end.year - years, end.month, end.day)

    # 从Yahoo Finance获取股票数据
    stock_data = yf.download(company_name, start, end)
    return stock_data


# 获取调整后的收盘价
def get_adjusted_close_price(company_name, years=3):
    stock_prices = get_stock_prices(company_name, years)
    if stock_prices is None:
        return None
    return stock_prices['Adj Close']


# 获取每家科技公司的股票计算移动平均线（MA） 20天
def get_moving_average(company_name, years=3):
    stock_prices = get_stock_prices(company_name, years)
    if stock_prices is None:
        return None
    return stock_prices['Adj Close'].rolling(window=20).mean()


# 示例用法
if __name__ == '__main__':
    # company_name TSLA NIO LCID AAPL
    company_name = 'TSLA'
    years = 3
    stock_prices = get_moving_average(company_name, years)
    print(stock_prices)
