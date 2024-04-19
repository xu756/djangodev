from django.contrib import admin

from webapp.models import User, Stock


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # 设置显示的字段
    list_display = ['id', 'user_name', 'password', 'email', 'gender']
    search_fields = ['user_name']
    list_per_page = 5
    list_max_show_all = 200
    list_filter = ['user_name', 'gender']
    list_display_links = ['user_name']
    pass


# 设置app的标题
admin.site.site_header = '我的Django项目'
admin.site.site_title = '我的Django项目'


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    # 设置显示的字段
    list_display = ['id', 'company_name', 'date', 'open', 'high', 'low', 'close', 'adj_close', 'volume']
    search_fields = ['company_name']
    list_per_page = 30
    list_max_show_all = 200
    list_display_links = ['company_name']
    pass
