from django.contrib import admin
from .models import header
from django.utils.html import format_html
class headerAdmin(admin.ModelAdmin):
    list_display = ('header_sub', 'header_title', 'header_des', 'header_des2', 'header_image','header_image2','header_image3','header_pr',)

admin.site.register(header, headerAdmin)



# Register your models here.
