
from django.utils.html import format_html
from .models import Students
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin



class StudentsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('الاسم', 'display_photo', 'photo', 'tel', 'data', 'gender', 'العنوان', 'mark', 'degree','الدفع')
    actions = ['download_image']

    def display_photo(self, obj):
        return format_html('<img src="{}" width="100" height="100" />'.format(obj.photo.url))

    display_photo.short_description = 'الصورة'

    def photo(self, obj):
        return obj.photo.url

    photo.short_description = 'رابط الصورة'

    def photo(self, obj):
        return obj.photo.url

    photo.short_description = 'رابط الصورة'



admin.site.register(Students, StudentsAdmin)



from .models import FormConfiguration

class FormConfigurationAdmin(admin.ModelAdmin):
    list_display = ['is_open']
    actions = ['open_form', 'close_form']

    def open_form(self, request, queryset):
        queryset.update(is_open=True)
    open_form.short_description = "Open Admission Form"

    def close_form(self, request, queryset):
        queryset.update(is_open=False)
    close_form.short_description = "Close Admission Form"

admin.site.register(FormConfiguration, FormConfigurationAdmin)