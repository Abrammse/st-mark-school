from django.contrib import admin
from .models import foot

class footAdmin(admin.ModelAdmin):
    list_display = ('foot_sub', 'foot_title',)

admin.site.register(foot, footAdmin)
# Register your models here.
