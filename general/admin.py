from django.contrib import admin
from .models import Courses, Level, Themes

@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    pass

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ['courses', 'name', 'number']


@admin.register(Themes)
class LevelAdmin(admin.ModelAdmin):
    list_display = ['courses', 'level', 'name', 'quantity', 'number']