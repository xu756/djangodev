from django.http import JsonResponse

from .data import get_stock_prices


def stock_data_view(request):
    # 公司名和年份
    company_name = 'TSLA'
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
    data = stock_prices.to_dict('records')

    # 返回JSON响应
    return JsonResponse(data, safe=False)
