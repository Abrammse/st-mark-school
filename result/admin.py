from django.contrib import admin
from .models import Student, Subject, Selector, FormConfiguration
from import_export.admin import ImportExportModelAdmin
from django.http import HttpResponse
from django.template.loader import get_template
import pdfkit

admin.site.register(Subject)
admin.site.register(Selector)


class StudentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'idschool', 'username', 'password', 'name', 'year', 'cla',
        'display_subjects', 'total_grade', 'results_open', 'التقديرالعام',
    )
    list_filter = ['results_open']

    def display_subjects(self, obj):
        return ', '.join([str(subject) for subject in obj.subjects.all()])

    def get_resul(self, obj):
        subjects = obj.subjects.all()
        if subjects:
            subject = subjects[0].subject
            return subject.resul
        return None

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        if not queryset.exists():
            queryset = Student.objects.none()
        return queryset, use_distinct

    search_fields = ['idschool', 'username', 'name']

    actions = ['open_results', 'close_results']

    def open_results(self, request, queryset):
        queryset.update(resul=True)

    def close_results(self, request, queryset):
        queryset.update(resul=False)

    open_results.short_description = "Open results for selected students"
    close_results.short_description = "Close results for selected students"


admin.site.register(Student, StudentAdmin)

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