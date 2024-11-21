from django.contrib import admin
from .models import Quiz, Question


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('name', 'sport', 'level', 'created_by')
    list_filter = ('sport', 'level')
    search_fields = ('name', 'sport')
    inlines = [QuestionInline]
