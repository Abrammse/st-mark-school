from django.contrib import admin
from .models import اللحان1
from .models import اللحان11
from .models import اللحان12
from .models import اللحان13
from .models import اللحان2
from .models import اللحان21
from .models import اللحان22
from .models import اللحان23
from .models import اللحان3
from .models import اللحان31
from .models import اللحان32
from .models import اللحان33
class اللحان1Admin(admin.ModelAdmin):
    list_display = (
    'واصف1', 'عنوان1', 'صورة1', 'واصف2', 'عنوان2', 'صورة2', 'واصف3',
    'عنوان3','صورة3',)
admin.site.register(اللحان1,اللحان1Admin)

class اللحان11Admin(admin.ModelAdmin):
    list_display = ('العنوان','الواصف','pdf','audios',)
admin.site.register(اللحان11,اللحان11Admin)

class اللحان12Admin(admin.ModelAdmin):
    list_display = ('العنوان','الواصف','pdf','audios',)
admin.site.register(اللحان12,اللحان12Admin)

class اللحان13Admin(admin.ModelAdmin):
    list_display = ('العنوان','الواصف','pdf','audios',)
admin.site.register(اللحان13,اللحان13Admin)
class اللحان2Admin(admin.ModelAdmin):
    list_display = (
    'واصف1', 'عنوان1', 'صورة1', 'واصف2', 'عنوان2', 'صورة2', 'واصف3',
    'عنوان3','صورة3',)
admin.site.register(اللحان2,اللحان2Admin)

class اللحان21Admin(admin.ModelAdmin):
    list_display = ('العنوان','الواصف','pdf','audios',)
admin.site.register(اللحان21,اللحان21Admin)

class اللحان22Admin(admin.ModelAdmin):
    list_display = ('العنوان','الواصف','pdf','audios',)
admin.site.register(اللحان22,اللحان22Admin)

class اللحان23Admin(admin.ModelAdmin):
    list_display = ('العنوان','الواصف','pdf','audios',)
admin.site.register(اللحان23,اللحان23Admin)
class اللحان3Admin(admin.ModelAdmin):
    list_display = (
    'واصف1', 'عنوان1', 'صورة1', 'واصف2', 'عنوان2', 'صورة2', 'واصف3',
    'عنوان3','صورة3',)
admin.site.register(اللحان3,اللحان3Admin)

class اللحان31Admin(admin.ModelAdmin):
    list_display = ('العنوان','الواصف','pdf','audios',)
admin.site.register(اللحان31,اللحان31Admin)

class اللحان32Admin(admin.ModelAdmin):
    list_display = ('العنوان','الواصف','pdf','audios',)
admin.site.register(اللحان32,اللحان32Admin)

class اللحان33Admin(admin.ModelAdmin):
    list_display = ('العنوان','الواصف','pdf','audios',)
admin.site.register(اللحان33,اللحان33Admin)
# Register your models here.
