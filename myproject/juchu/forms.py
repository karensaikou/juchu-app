from django.forms import ModelForm , DateInput

from .models import Order


class OrderForm( ModelForm ):
    class Meta :
        model = Order
        fields = [
            "product_name" , "order_date" , "requested_delivery_date" ,
            "number_of_orders" ,  
            "shipping_date" , "actual_delivery_date",
            "vehicle_dispatch" ]
        widgets = {"order_date":DateInput(attrs = {"type":"date"}),
                   "requested_delivery_date":DateInput(attrs = {"type":"date"}),
                   "shipping_date":DateInput( attrs ={"type":"date"}),
                   "actual_delivery_date":DateInput( attrs = {"type":"date"})}


#"order_unit" 
#"stock_quantity"
#"material_delivery_date",
#"production_completion_date" ,
#"customer"
#"delivery_address"