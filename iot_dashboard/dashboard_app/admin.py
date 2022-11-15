from django.contrib import admin
from .models import User_Data,DeviceDetails

# Register your models here.


class UserAdmin(admin.ModelAdmin):
	list_display = ['username','email','password1','password2']

admin.site.register(User_Data,UserAdmin)


class DeviceDetailsAdmin(admin.ModelAdmin):
	list_display = ['userID','status','devicetype','name']

admin.site.register(DeviceDetails,DeviceDetailsAdmin)