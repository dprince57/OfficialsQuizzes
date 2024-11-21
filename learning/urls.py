from django.urls import path
from .views import LearningPathListView, UserProgressView

urlpatterns = [
    path('', LearningPathListView.as_view(), name='learning-paths'),
    path('progress/', UserProgressView.as_view(), name='user-progress'),
]
