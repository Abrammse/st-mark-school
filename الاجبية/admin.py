from django.contrib import admin
from .models import الاجبية1
from .models import الاجبية11
from .models import الاجبية12
from .models import الاجبية13
from .models import الاجبية2
from .models import الاجبية21
from .models import الاجبية22
from .models import الاجبية23
from .models import الاجبية3
from .models import الاجبية31
from .models import الاجبية32
from .models import الاجبية33
class الاجبية1Admin(admin.ModelAdmin):
    list_display = (
    'واصف1', 'عنوان1', 'صورة1', 'واصف2', 'عنوان2', 'صورة2', 'واصف3',
    'عنوان3','صورة3',)
admin.site.register(الاجبية1,الاجبية1Admin)

class الاجبية11Admin(admin.ModelAdmin):
    list_display = ('العنوان','الواصف','pdf','audios',)
admin.site.register(الاجبية11,الاجبية11Admin)

class الاجبية12Admin(admin.ModelAdmin):
    list_display = ('العنوان','الواصف','pdf','audios',)
admin.site.register(الاجبية12,الاجبية12Admin)

class الاجبية13Admin(admin.ModelAdmin):
    list_display = ('العنوان','الواصف','pdf','audios',)
admin.site.register(الاجبية13,الاجبية13Admin)
class الاجبية2Admin(admin.ModelAdmin):
    list_display = (
    'واصف1', 'عنوان1', 'صورة1', 'واصف2', 'عنوان2', 'صورة2', 'واصف3',
    'عنوان3','صورة3',)
admin.site.register(الاجبية2,الاجبية2Admin)

class الاجبية21Admin(admin.ModelAdmin):
    list_display = ('العنوان','الواصف','pdf','audios',)
admin.site.register(الاجبية21,الاجبية21Admin)

class الاجبية22Admin(admin.ModelAdmin):
    list_display = ('العنوان','الواصف','pdf','audios',)
admin.site.register(الاجبية22,الاجبية22Admin)

class الاجبية23Admin(admin.ModelAdmin):
    list_display = ('العنوان','الواصف','pdf','audios',)
admin.site.register(الاجبية23,الاجبية23Admin)

class الاجبية3Admin(admin.ModelAdmin):
    list_display = (
    'واصف1', 'عنوان1', 'صورة1', 'واصف2', 'عنوان2', 'صورة2', 'واصف3',
    'عنوان3','صورة3',)
admin.site.register(الاجبية3,الاجبية3Admin)

class الاجبية31Admin(admin.ModelAdmin):
    list_display = ('العنوان','الواصف','pdf','audios',)
admin.site.register(الاجبية31,الاجبية31Admin)

class الاجبية32Admin(admin.ModelAdmin):
    list_display = ('العنوان','الواصف','pdf','audios',)
admin.site.register(الاجبية32,الاجبية32Admin)

class الاجبية33Admin(admin.ModelAdmin):
    list_display = ('العنوان','الواصف','pdf','audios',)
admin.site.register(الاجبية33,الاجبية33Admin)
# Register your models here.
