from django.contrib import admin
from .models import الاية
class الايةAdmin(admin.ModelAdmin):
    list_display = ('الاية' , )
admin.site.register(الاية,الايةAdmin)
# Register your models here.
