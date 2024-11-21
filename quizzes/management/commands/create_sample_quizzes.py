from django.core.management.base import BaseCommand
from quizzes.models import Quiz, Question


class Command(BaseCommand):
    help = "Create sample quizzes with questions for testing"

    def handle(self, *args, **kwargs):
        quiz, created = Quiz.objects.get_or_create(
            name="Sample NCAA Football Quiz",
            sport="NCAA Football",
            level="beginner"
        )

        questions = [
            {
                "text": "How many players are allowed on the field per team?",
                "correct_answer": "11",
                "rule_reference": "Rule 1-1-1"
            },
            {
                "text": "What happens if a team calls a timeout when it has none left?",
                "correct_answer": "Delay of game penalty",
                "rule_reference": "Rule 3-3-4"
            }
        ]

        for q in questions:
            Question.objects.get_or_create(
                quiz=quiz,
                text=q["text"],
                correct_answer=q["correct_answer"],
                rule_reference=q["rule_reference"]
            )

        self.stdout.write(self.style.SUCCESS('Sample quizzes and questions created!'))
