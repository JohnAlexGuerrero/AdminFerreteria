from django.contrib import admin

from employed.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','first_name','last_name','email','address','phones')
    
    def phones(self, obj):
        return f'{obj.phone_one} - {obj.phone_two}'
