from django.contrib import admin
from django.urls import path 
from . import views

app_name = "juchu"



urlpatterns = [
    path( "" , views.index , name = "index") ,
    path("order/create/" , views.order_create , name = "order_create"),
    path("order/list/" , views.order_list , name = "order_list"),
    path("order/detail/<uuid:id_sagasu>/" , views.order_detail , name = "order_detail"),
    path("order/update/<uuid:id_sagasu>/" , views.order_update , name = "order_update"),
    path("order/delete/<uuid:id_sagasu>/" , views.order_delete , name = "order_delete"),
]
