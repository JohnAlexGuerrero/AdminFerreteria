from django.contrib import admin
from datetime import datetime
from django.db.models import Sum

from shopping.models import Providers, Invoice, Order, PriceProducts

from inventory.models import Product

@admin.register(Invoice)
class InvoicesAdmin(admin.ModelAdmin):
    list_display = ('number','provider','created_at','expiration_at','total','items','days','status')
    
    invoice_arr = []
    
    ordering = ('created_at',)
    
    search_fields = ('providers',)
    
    def days(self, obj):
        now = datetime.now()
        days = (datetime.strptime(str(obj.expiration_at), "%Y-%m-%d") - now).days
        return days
    
    def status(self, obj):
        # invoices = [ invoice.number for invoice in PaidShopping.objects.all()[:5]]
        
        return "Pending" if (obj.total) != 0 else "Paid"

    def items(self, obj):
        return Order.objects.filter(invoice__id=obj.id).count()
    
@admin.register(Providers)
class ProvidersAdmin(admin.ModelAdmin):
    list_display = ('name','address')
    

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('display_provider','invoice', 'product','created_at')
    
    ordering = ('created_at',)
    
    def display_provider(self, obj):
        return obj.invoice.provider


@admin.register(PriceProducts)
class PriceProductsAdmin(admin.ModelAdmin):
    list_display = ('order','display_reference','price','display_unit_measure')
    
    
    def display_reference(self, obj):
        return obj.order.reference
    
    def display_unit_measure(self, obj):
        return obj.order.product.unit_measure
    
    display_reference.short_description = 'referencia'
    display_unit_measure.short_description = 'unidad'






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