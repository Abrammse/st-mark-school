from django.contrib import admin
from .models import الاخبار
class الاخبارAdmin(admin.ModelAdmin):
    list_display = ('القسم','العنوان','الواصف','الصورة')
admin.site.register(الاخبار,الاخبارAdmin)

# Register your models here.

