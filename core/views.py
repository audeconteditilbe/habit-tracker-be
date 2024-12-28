from django.http import Http404
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
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

    def get(self, request, format=None):
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

class HabitDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, request, pk):
        try:
            return Habit.objects.filter(author=request.user).get(pk=pk)
        except Habit.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        habit = self.get_object(request, pk)
        serializer = HabitSerializer(habit)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        habit = self.get_object(request, pk)
        serializer = HabitSerializer(habit, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        habit = self.get_object(request, pk)
        habit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EntryListCreate(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        entries = Entry.objects.all()
        serializer = EntrySerializer(entries, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EntryDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Entry.objects.get(pk=pk)
        except Entry.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        entry = self.get_object(pk)
        serializer = EntrySerializer(entry)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        entry = self.get_object(pk)
        serializer = EntrySerializer(entry, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        entry = self.get_object(pk)
        entry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)