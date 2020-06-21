from django.contrib import admin
from .models import Application, Interview, Skills

# Register your models here.
admin.site.register(Application)
admin.site.register(Interview)
admin.site.register(Skills)