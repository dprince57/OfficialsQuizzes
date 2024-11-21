from rest_framework import serializers
from .models import LearningPath, LearningModule, UserProgress

class LearningModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningModule
        fields = '__all__'

class LearningPathSerializer(serializers.ModelSerializer):
    modules = LearningModuleSerializer(many=True, read_only=True)

    class Meta:
        model = LearningPath
        fields = ['id', 'sport', 'level', 'description', 'modules']

class UserProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProgress
        fields = ['user', 'completed_modules', 'points', 'badges']
