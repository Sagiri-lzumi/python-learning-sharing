""""定义learn_urls.logs的url文件格式"""

from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    #main page
    path('', views.index, name='index'),
]
