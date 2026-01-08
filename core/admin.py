from django.contrib import admin
from .models import Task, BrainDumpItem, TaskList, ListItem, UserSettings, Subscription

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'task_type', 'is_done', 'created_at')
    list_filter = ('task_type', 'is_done')

@admin.register(BrainDumpItem)
class BrainDumpItemAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_at')

@admin.register(TaskList)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

@admin.register(ListItem)
class ListItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'tasklist', 'is_done', 'created_at')

@admin.register(UserSettings)
class UserSettingsAdmin(admin.ModelAdmin):
    list_display = ('user', 'theme', 'icon_color')

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'is_active', 'valid_until', 'created_at')