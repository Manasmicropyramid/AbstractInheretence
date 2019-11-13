from django.contrib import admin
from .models import Father,Mother,Son

class AdminFather(admin.ModelAdmin):
    list_display = ['fname','email','mobile','location','salary']

class AdminMother(admin.ModelAdmin):
    list_display = ['mname','email','mobile','location','salary']

class AdminSon(admin.ModelAdmin):
    list_display = ['sname','email','mobile','location','salary']

admin.site.register(Father,AdminFather)
admin.site.register(Mother,AdminMother)
admin.site.register(Son,AdminSon)