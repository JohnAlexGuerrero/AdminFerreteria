from django.contrib import admin

from store.models import UserStore, Store

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name','nit','address','email','phones')
    
    def phones(self, obj):
        return obj.whatsapp
    
@admin.register(UserStore)
class UserStoreAdmin(admin.ModelAdmin):
    list_display = ('store','user')

