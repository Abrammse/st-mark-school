from django.contrib import admin
from .models import الخدام
class الخدامAdmin(admin.ModelAdmin):
    list_display = ( 'اسمه', 'دوره', 'الصورة',)

admin.site.register(الخدام,الخدامAdmin)
# Register your models here.
