from django.shortcuts import render , redirect ,get_object_or_404
from django.views import View
from .models import Order
from .forms import OrderForm
from datetime import datetime , date
from zoneinfo import ZoneInfo


class IndexView( View ):
    def get ( self , request):

        datetime_now_python = datetime.now( ZoneInfo ( "Asia/Tokyo")).strftime( "%Y年 %m月 %d日")
        return render( request , "index.html" , {"datetime_now_html" : datetime_now_python})
    

class OrderCreateView(View):
    def get( self , request ):
        create_python = OrderForm()
        return render( request , "order_create.html" , {"create_html" : create_python })
    
    def post( self , request ):
        create_python = OrderForm( request.POST )
        if create_python.is_valid():
            create_python.save()
            return redirect( "juchu:index")
        
        return render( request , "order_create.html" , {"create_html" : create_python})


class OrderListView(View):
    def get( self , request ):
        list_python = Order.objects.order_by("order_date")

        for i in list_python :
            i.is_delivered =(
                i.actual_delivery_date is not None and
                i.actual_delivery_date <= date.today()
            )
        return render( request , "order_list.html" , {"list_html" : list_python})


class OrderDetailView(View):
    def get( self , request , id_sagasu):
        detail_python = get_object_or_404( Order , id = id_sagasu)
        return render( request , "order_detail.html" , {"detail_html":detail_python})

class OrderUpdateView(View):
    def get( self , request , id_sagasu):
        data = get_object_or_404( Order , id = id_sagasu)
        update_python = OrderForm( instance = data)
        return render( request , "order_update.html" , {"update_html":update_python , "order":data})
    
    def post( self , request , id_sagasu):
        data = get_object_or_404( Order , id = id_sagasu)
        update_python = OrderForm( request.POST , instance = data )
        if update_python.is_valid():
            update_python.save()
            return redirect( "juchu:order_detail" , id_sagasu = id_sagasu)
        
        return render( request , "order_create.html" , {"create_html":update_python})

class OrderDeleteView(View):
    def get( self , request , id_sagasu):
        delete_python = get_object_or_404( Order , id = id_sagasu)
        return render( request , "order_delete.html" , {"delete_html":delete_python})
    
    def post( self , request , id_sagasu):
        delete_python = get_object_or_404( Order , id = id_sagasu)
        delete_python.delete()
        return redirect( "juchu:order_list")


index = IndexView.as_view()
order_create = OrderCreateView.as_view()
order_list = OrderListView.as_view()
order_detail = OrderDetailView.as_view()
order_update = OrderUpdateView.as_view()
order_delete = OrderDeleteView.as_view()