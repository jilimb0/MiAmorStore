from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('t-shirts/', views.tshirts, name="t-shirts"),
    path('shoppers/', views.shoppers, name="shoppers"),
    path('sweatshirts/', views.sweatshirts, name="sweatshirts"),
    path('notes/', views.notes, name="notes"),
    path('stickers/', views.stickers, name="stickers"),
    path('constructor/', views.constructor, name="constructor"),
    path('login/', views.login, name="login"),
]
