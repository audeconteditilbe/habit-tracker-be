from django.http import HttpRequest
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Entry, Habit
from .serializers import EntrySerializer, HabitSerializer, UserSerializer

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class HabitListCreate(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: HttpRequest, format=None):
        habits = Habit.objects.filter(author=request.user)
        serializer = HabitSerializer(habits, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HabitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EntryListCreate(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: HttpRequest, format=None):
        entries = Entry.objects.all()
        serializer = EntrySerializer(entries, many=True)
        return Response(serializer.data)

    def post(self, request: HttpRequest, format=None):
        serializer = EntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
