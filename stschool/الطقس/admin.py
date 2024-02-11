from django.contrib import admin
from .models import الطقس1
from .models import الطقس11
from .models import الطقس12
from .models import الطقس13
from .models import الطقس2
from .models import الطقس21
from .models import الطقس22
from .models import الطقس23
from .models import الطقس3
from .models import الطقس31
from .models import الطقس32
from .models import الطقس33
class الطقس1Admin(admin.ModelAdmin):
    list_display = (
    'واصف1', 'عنوان1', 'صورة1', 'واصف2', 'عنوان2', 'صورة2', 'واصف3',
    'عنوان3','صورة3',)
admin.site.register(الطقس1,الطقس1Admin)

class الطقس11Admin(admin.ModelAdmin):
    list_display = ('العنوان','الواصف','pdf','audios',)
admin.site.register(الطقس11,الطقس11Admin)

class الطقس12Admin(admin.ModelAdmin):
    list_display = ('العنوان','الواصف','pdf','audios',)
admin.site.register(الطقس12,الطقس12Admin)

class الطقس13Admin(admin.ModelAdmin):
    list_display = ('العنوان','الواصف','pdf','audios',)
admin.site.register(الطقس13,الطقس13Admin)
class الطقس2Admin(admin.ModelAdmin):
    list_display = (
    'واصف1', 'عنوان1', 'صورة1', 'واصف2', 'عنوان2', 'صورة2', 'واصف3',
    'عنوان3','صورة3',)
admin.site.register(الطقس2,الطقس2Admin)

class الطقس21Admin(admin.ModelAdmin):
    list_display = ('العنوان','الواصف','pdf','audios',)
admin.site.register(الطقس21,الطقس21Admin)

class الطقس22Admin(admin.ModelAdmin):
    list_display = ('العنوان','الواصف','pdf','audios',)
admin.site.register(الطقس22,الطقس22Admin)

class الطقس23Admin(admin.ModelAdmin):
    list_display = ('العنوان','الواصف','pdf','audios',)
admin.site.register(الطقس23,الطقس23Admin)
class الطقس3Admin(admin.ModelAdmin):
    list_display = (
    'واصف1', 'عنوان1', 'صورة1', 'واصف2', 'عنوان2', 'صورة2', 'واصف3',
    'عنوان3','صورة3',)
admin.site.register(الطقس3,الطقس3Admin)

class الطقس31Admin(admin.ModelAdmin):
    list_display = ('العنوان','الواصف','pdf','audios',)
admin.site.register(الطقس31,الطقس31Admin)

class الطقس32Admin(admin.ModelAdmin):
    list_display = ('العنوان','الواصف','pdf','audios',)
admin.site.register(الطقس32,الطقس32Admin)

class الطقس33Admin(admin.ModelAdmin):
    list_display = ('العنوان','الواصف','pdf','audios',)
admin.site.register(الطقس33,الطقس33Admin)
# Register your models here.
