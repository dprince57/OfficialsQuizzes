from django.contrib import admin
from .models import LearningPath, LearningModule, UserProgress


class LearningModuleInline(admin.TabularInline):
    model = LearningModule
    extra = 1


@admin.register(LearningPath)
class LearningPathAdmin(admin.ModelAdmin):
    list_display = ('sport', 'level', 'description', 'created_at')
    list_filter = ('sport', 'level')
    search_fields = ('sport', 'level', 'description')
    inlines = [LearningModuleInline]


@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'points')
    search_fields = ('user__username',)
