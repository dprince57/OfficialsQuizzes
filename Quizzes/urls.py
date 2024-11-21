from django.urls import path
from .views import QuizListView, QuizCreateView, QuestionCreateView

urlpatterns = [
    path('', QuizListView.as_view(), name='quiz-list'),
    path('create/', QuizCreateView.as_view(), name='quiz-create'),
    path('<int:quiz_id>/questions/create/', QuestionCreateView.as_view(), name='question-create'),
]
