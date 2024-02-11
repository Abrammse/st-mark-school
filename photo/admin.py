from django.contrib import admin

from django.utils.html import format_html

from .models import الصور
from .models import الصورة
class الصورAdmin(admin.ModelAdmin):
    list_display = ('الكلمة', 'عدد', 'التاريخ', 'المناسبة')
admin.site.register(الصور, الصورAdmin)





class الصورةAdmin(admin.ModelAdmin):
    list_display = ('display_image', 'related_الصور')

    def display_image(self, obj):
        if obj.الصورة:
            return format_html('<img src="{}" width="100" height="100" />'.format(obj.الصورة.url))
        else:
            return 'No Image'
    display_image.short_description = 'Image'

    def related_الصور(self, obj):
        return obj.الصور
    related_الصور.short_description = 'Related الصور'


admin.site.register(الصورة, الصورةAdmin)