from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated


from tasks.models import TaskUserRel
from tasks.serializers import TaskUserRelSerializer


class TaskListView(ListAPIView):
	serializer_class = TaskUserRelSerializer
	permission_classes = [IsAuthenticated]	
	

	def get_queryset(self):
		return TaskUserRel.objects.filter(user=self.request.user)
