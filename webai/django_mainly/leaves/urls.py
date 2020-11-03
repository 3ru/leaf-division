from django.urls import path
from . import views

app_name = 'leaves'
urlpatterns = [
    path('', views.index, name='index'),
    path('predict/', views.predict, name='predict'),
    path('test/', views.test, name='test'),
]