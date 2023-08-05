from django.contrib import admin
from datetime import datetime
from django.db.models import Sum

from shopping.models import Providers, Invoice, Order, PriceProducts, Payment

from inventory.models import Product

@admin.register(Invoice)
class InvoicesAdmin(admin.ModelAdmin):
    list_display = ('number','provider','created_at','expiration_at','total','display_balance','items','days','status')
    
    invoice_arr = []
    
    ordering = ('created_at',)
    
    search_fields = ('provider__name',)
    
    def days(self, obj):
        now = datetime.now()
        days = (datetime.strptime(str(obj.expiration_at), "%Y-%m-%d") - now).days
        return days
    
    def status(self, obj):
        pays = Payment.objects.annotate(balance_sum=Sum('total')).filter(invoice__number=obj.number)
        
        if len(pays) != 0:
            print(pays[0].balance_sum)
            return "Pending" if (obj.total - pays[0].balance_sum) != 0 else "Paid"
   
        return "Pending"

    def items(self, obj):
        return Order.objects.filter(invoice__id=obj.id).count()
    
    def display_balance(self, obj): #Book.objects.annotate(num_authors=Count("authors")).filter(num_authors__gt=1)
        total_pays = Payment.objects.annotate(value=Sum('total')).filter(invoice__number=obj.number)
        return (obj.total - total_pays[0].value) if len(total_pays) != 0 else obj.total
    
    display_balance.short_description = 'saldo'
    
@admin.register(Providers)
class ProvidersAdmin(admin.ModelAdmin):
    list_display = ('name','address')
    

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('display_provider','invoice', 'product','created_at')
    
    ordering = ('-created_at',)
    
    def display_provider(self, obj):
        return obj.invoice.provider


@admin.register(PriceProducts)
class PriceProductsAdmin(admin.ModelAdmin):
    list_display = ('order','display_reference','price','display_stock','display_unit_measure')
    
    
    def display_reference(self, obj):
        return obj.order.reference
    
    def display_unit_measure(self, obj):
        return obj.order.product.unit_measure
    
    def display_stock(self,obj):
        return obj.order.quantity
    
    display_reference.short_description = 'referencia'
    display_stock.short_description = 'avalible'
    display_unit_measure.short_description = 'unidad'



@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('number','invoice','created_at','total','balance','comments')



# @admin.register(ProductInvoice)
# class ProductInvoiceAdmin(admin.ModelAdmin):
#     list_display = ('product','quantity','get_unit_measure','price','get_value_total','get_date_created',)

#     def get_value_total(self, obj):
#         return obj.price * obj.quantity

#     def get_unit_measure(self, obj):
#         product = Product.objects.get(name=obj)
#         return product.unit_measure
    
#     def get_date_created(self,obj):
#         invoice = Invoice.objects.get(number=obj)
#         return 23

#     get_value_total.short_description = 'total'
#     get_unit_measure.short_description = 'unidad'
#     get_date_created.short_description = 'created'