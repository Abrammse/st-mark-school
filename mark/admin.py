from django.contrib import admin
from .models import mark
class markAdmin(admin.ModelAdmin):
    list_display = ('mark_sub','mark_title','mark_image')
admin.site.register(mark, markAdmin)
# Register your models here.
