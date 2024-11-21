from django.db import models

class Quiz(models.Model):
    name = models.CharField(max_length=255)
    sport = models.CharField(max_length=50)  # E.g., "NCAA Football", "NFHS Basketball"
    level = models.CharField(max_length=50, choices=[('beginner', 'Beginner'), ('advanced', 'Advanced')])

    def __str__(self):
        return f"{self.name} ({self.sport} - {self.level})"

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    text = models.TextField()
    correct_answer = models.CharField(max_length=255)
    rule_reference = models.TextField()

    def __str__(self):
        return self.text
