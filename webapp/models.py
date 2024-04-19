from django.db import models

choices = (
    ('男', '男性'),
    ('女', '女性'),
)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100, default='user', verbose_name="用户名")
    password = models.CharField(max_length=100, default='123456', verbose_name="密码")
    email = models.EmailField(max_length=100, default='email@qq.com', verbose_name="邮箱")
    gender = models.CharField(max_length=2, choices=choices, default='男', verbose_name='性别')

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = 'user'
        verbose_name = '用户列表'
        verbose_name_plural = verbose_name


# 创建一个模型类
# 保存

#     'Date': 'date',
#     'Open': 'open',
#     'High': 'high',
#     'Low': 'low',
#     'Close': 'close',
#     'Adj Close': 'adj_close',
#     'Volume': 'volume',

class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100, default='TSLA', verbose_name="公司名")
    date = models.DateField(verbose_name='日期')
    open = models.FloatField(verbose_name='开盘价')
    high = models.FloatField(verbose_name='最高价')
    low = models.FloatField(verbose_name='最低价')
    close = models.FloatField(verbose_name='收盘价')
    adj_close = models.FloatField(verbose_name='调整后的收盘价')
    volume = models.FloatField(verbose_name='成交量')

    def __str__(self):
        return self.company_name

    class Meta:
        db_table = 'stock'
        verbose_name = '股票列表'
        verbose_name_plural = verbose_name

    #         添加数据
    def add_data(self, company_name, date, open, high, low, close, adj_close, volume):
        #  先根据时间和公司名查询是否有数据，如果有则更新，没有则添加
        stock = Stock.objects.filter(company_name=company_name, date=date)
        if stock:
            stock.update(company_name=company_name, date=date, open=open, high=high, low=low, close=close,
                         adj_close=adj_close, volume=volume)
        else:
            stock = Stock.objects.create(company_name=company_name, date=date, open=open, high=high,
                                         low=low,
                                         close=close, adj_close=adj_close, volume=volume)
            stock.save()
        return self
