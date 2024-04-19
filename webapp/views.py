from django.http import JsonResponse

from .data import *


# path('stock_data/<str:company_name>', stock_data_view, name='stock_data_view'),
def stock_data_view(request, company_name):
    # 公司名和年份
    # company_name = request.GET.get('company_name', 'TSLA')
    years = 1

    # 使用函数获取股票价格和移动平均线数据
    stock_prices = get_stock_prices(company_name, years)

    stock_prices.index = stock_prices.index.strftime('%Y-%m-%d')
    stock_prices = stock_prices.reset_index()
    stock_prices.rename(columns={
        'Date': 'date',
        'Open': 'open',
        'High': 'high',
        'Low': 'low',
        'Close': 'close',
        'Adj Close': 'adj_close',
        'Volume': 'volume',
    }, inplace=True)
    stock_prices = stock_prices.dropna()
    data = stock_prices.to_dict('records')
    return JsonResponse(data, safe=False)


def get_moving_average_view(request, company_name):
    # 公司名和年份
    # company_name = request.GET.get('company_name', 'TSLA')
    years = 1

    # 使用函数获取股票价格和移动平均线数据
    stock_prices = get_moving_average(company_name, years)

    stock_prices.index = stock_prices.index.strftime('%Y-%m-%d')
    stock_prices = stock_prices.reset_index()
    stock_prices.rename(columns={
        'Date': 'date',
        'Adj Close': 'ma',
    }, inplace=True)
    stock_prices = stock_prices.dropna()
    data = stock_prices.to_dict('records')
    return JsonResponse(data, safe=False)


# 日收益率
def daily_return_view(request, company_name):
    # 公司名和年份
    years = 1
    # 使用函数获取股票价格和移动平均线数据
    stock_prices = get_daily_return(company_name, years)

    stock_prices.index = stock_prices.index.strftime('%Y-%m-%d')
    stock_prices = stock_prices.reset_index()
    print(stock_prices.info())
    stock_prices.rename(columns={
        'Date': 'date',
        'Adj Close': 'daily_return',
    }, inplace=True)
    #  删除 daily_return 为NaN的
    stock_prices = stock_prices.dropna()
    data = stock_prices.to_dict('records')
    return JsonResponse(data, safe=False)
