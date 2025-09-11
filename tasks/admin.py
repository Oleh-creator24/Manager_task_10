from django.contrib import admin
from .models import Status, Task, SubTask

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'deadline']
    list_filter = ['status', 'deadline']
    search_fields = ['title', 'description']
    date_hierarchy = 'deadline'

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'task', 'status', 'deadline']
    list_filter = ['status', 'deadline']
    search_fields = ['title', 'description']
    date_hierarchy = 'deadline'
