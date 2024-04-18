from django.http import JsonResponse

from .data import get_stock_prices


def stock_data_view(request):
    # 公司名和年份
    company_name = 'TSLA'
    years = 1

    # 使用函数获取股票价格和移动平均线数据
    stock_prices = get_stock_prices(company_name, years)
    print(stock_prices.columns.values.tolist())
    # 将数据转换为JSON格式
    data = {
        'success': True,
        'data': {
            'index': stock_prices.index.values.tolist(),
            'open': stock_prices["Open"].tolist(),
            'high': stock_prices["High"].tolist(),
            'low': stock_prices["Low"].tolist(),
            'close': stock_prices["Close"].tolist(),
            'adjclose': stock_prices["Adj Close"].tolist(),
            'volume': stock_prices["Volume"].tolist(),

        }
    }

    # 返回JSON响应
    return JsonResponse(data)
