from django.contrib import admin
from .models import Student, Subject, Selector, FormConfiguration

admin.site.register(Subject)
admin.site.register(Selector)


class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'idschool', 'username', 'name', 'year', 'cla',
        'display_subjects', 'total_grade',  'resul' ,'التقديرالعام',
    )

    def display_subjects(self, obj):
        return ', '.join([str(subject) for subject in obj.subjects.all()])

    def get_resul(self, obj):
        subjects = obj.subjects.all()
        if subjects:
            subject = subjects[0].subject
            return subject.resul
        return None


admin.site.register(Student, StudentAdmin)

actions = ['open_results', 'close_results']


def open_results(self, request, queryset):
    queryset.update(resul=True)


def close_results(self, request, queryset):
    queryset.update(resul=False)


open_results.short_description = "Open results for selected students"
close_results.short_description = "Close results for selected students"

