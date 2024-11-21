from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import LearningPath, LearningModule, UserProgress
from .serializers import LearningPathSerializer, LearningModuleSerializer, UserProgressSerializer
from rest_framework.permissions import IsAuthenticated

class LearningPathListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        sport = request.query_params.get('sport', None)
        paths = LearningPath.objects.filter(sport=sport) if sport else LearningPath.objects.all()
        serializer = LearningPathSerializer(paths, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserProgressView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        progress, created = UserProgress.objects.get_or_create(user=request.user)
        serializer = UserProgressSerializer(progress)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        progress, created = UserProgress.objects.get_or_create(user=request.user)
        module_id = request.data.get('module_id')
        try:
            module = LearningModule.objects.get(id=module_id)
        except LearningModule.DoesNotExist:
            return Response({"error": "Module not found"}, status=status.HTTP_404_NOT_FOUND)

        if module not in progress.completed_modules.all():
            progress.completed_modules.add(module)
            progress.points += 10  # Award points for completing a module
            progress.save()

        return Response({"message": "Module completed successfully"}, status=status.HTTP_200_OK)
