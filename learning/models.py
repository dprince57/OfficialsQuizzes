from django.db import models
from users.models import User


class LearningPath(models.Model):
    sport = models.CharField(max_length=50)  # e.g., "NCAA Football"
    level = models.CharField(
        max_length=50,
        choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')]
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sport} - {self.level}"


class LearningModule(models.Model):
    path = models.ForeignKey(LearningPath, on_delete=models.CASCADE, related_name="modules")
    title = models.CharField(max_length=255)
    content = models.TextField()  # Can include video links or instructional text
    quiz_id = models.IntegerField(null=True, blank=True)  # Links to a Quiz in the `quizzes` app

    def __str__(self):
        return self.title


class UserProgress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="progress")
    completed_modules = models.ManyToManyField(LearningModule, blank=True)
    points = models.IntegerField(default=0)
    badges = models.JSONField(default=list)  # Stores earned badges as a list of strings

    def __str__(self):
        return f"{self.user.username} - {self.points} points"
