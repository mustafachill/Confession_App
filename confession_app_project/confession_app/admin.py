from django.contrib import admin
from confession_app.models import Confession
# Register your models here.

class ConfessionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Message Group',{"fields":["message"]}),
        ('Nickname Group',{"fields":["nickname"]})
    ]
    #fields = ['nickname','message']


admin.site.register(Confession, ConfessionAdmin)