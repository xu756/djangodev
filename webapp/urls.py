from django.urls import path

from webapp.views import *

urlpatterns = [
    path('stock_data/', stock_data_view, name='stock_data_view'),
]
