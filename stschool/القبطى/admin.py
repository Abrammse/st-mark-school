from django.contrib import admin
from .models import القبطى1
from .models import القبطى11
from .models import القبطى12
from .models import القبطى13
from .models import القبطى2
from .models import القبطى21
from .models import القبطى22
from .models import القبطى23
from .models import القبطى3
from .models import القبطى31
from .models import القبطى32
from .models import القبطى33
class القبطى1Admin(admin.ModelAdmin):
    list_display = (
    'واصف1', 'عنوان1', 'صورة1', 'واصف2', 'عنوان2', 'صورة2', 'واصف3',
    'عنوان3','صورة3',)
admin.site.register(القبطى1,القبطى1Admin)

class القبطى11Admin(admin.ModelAdmin):
    list_display = ('العنوان','الواصف','pdf','audios',)
admin.site.register(القبطى11,القبطى11Admin)

class القبطى12Admin(admin.ModelAdmin):
    list_display = ('العنوان','الواصف','pdf','audios',)
admin.site.register(القبطى12,القبطى12Admin)

class القبطى13Admin(admin.ModelAdmin):
    list_display = ('العنوان','الواصف','pdf','audios',)
admin.site.register(القبطى13,القبطى13Admin)
class القبطى2Admin(admin.ModelAdmin):
    list_display = (
    'واصف1', 'عنوان1', 'صورة1', 'واصف2', 'عنوان2', 'صورة2', 'واصف3',
    'عنوان3','صورة3',)
admin.site.register(القبطى2,القبطى2Admin)

class القبطى21Admin(admin.ModelAdmin):
    list_display = ('العنوان','الواصف','pdf','audios',)
admin.site.register(القبطى21,القبطى21Admin)

class القبطى22Admin(admin.ModelAdmin):
    list_display = ('العنوان','الواصف','pdf','audios',)
admin.site.register(القبطى22,القبطى22Admin)

class القبطى23Admin(admin.ModelAdmin):
    list_display = ('العنوان','الواصف','pdf','audios',)
admin.site.register(القبطى23,القبطى23Admin)

class القبطى3Admin(admin.ModelAdmin):
    list_display = (
    'واصف1', 'عنوان1', 'صورة1', 'واصف2', 'عنوان2', 'صورة2', 'واصف3',
    'عنوان3','صورة3',)
admin.site.register(القبطى3,القبطى3Admin)

class القبطى31Admin(admin.ModelAdmin):
    list_display = ('العنوان','الواصف','pdf','audios',)
admin.site.register(القبطى31,القبطى31Admin)

class القبطى32Admin(admin.ModelAdmin):
    list_display = ('العنوان','الواصف','pdf','audios',)
admin.site.register(القبطى32,القبطى32Admin)

class القبطى33Admin(admin.ModelAdmin):
    list_display = ('العنوان','الواصف','pdf','audios',)
admin.site.register(القبطى33,القبطى33Admin)
# Register your models here.
