from django.db import models 

import uuid


class DispatchStatus(models.TextChoices):
    DONE = "done" , "完了"
    NOT_DONE = "not_done" , "未了"

class Order(models.Model):
    id = models.UUIDField( primary_key = True , default = uuid.uuid4 , editable = False , verbose_name = "ID") 
    product_name = models.CharField( max_length = 20 , verbose_name = "製品名") #営業
    order_date = models.DateField( verbose_name = "受注日") #営業
    requested_delivery_date = models.DateField( verbose_name = "希望納期") #営業
    number_of_orders = models.IntegerField( verbose_name = "受注数量") #営業
    shipping_date = models.DateField( null=True, blank=True , verbose_name = "出荷日") #生産管理
    actual_delivery_date = models.DateField( null=True, blank=True , verbose_name = "納入日") #生産管理
    vehicle_dispatch = models.CharField( null=True, blank=True , max_length = 10 , choices = DispatchStatus.choices , verbose_name = "配車状況") #物流
    created_at = models.DateTimeField( auto_now_add = True , verbose_name = "作成日時")
    updated_at = models.DateTimeField( auto_now = True , verbose_name = "更新日時")

    def __str__(self):
        return self.product_name