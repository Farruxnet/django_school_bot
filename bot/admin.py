from django.contrib import admin
from . models import Category, Teacher, About

class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'about')

admin.site.site_header = 'Boshqaruv paneli'
admin.site.site_title = 'Boshqaruv paneli'
admin.site.index_title = "Assalomu alaykum!"
admin.site.register(Category, CategoryAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(About, AboutAdmin)

