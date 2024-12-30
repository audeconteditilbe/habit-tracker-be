from datetime import  datetime, timedelta

from django.http import Http404
from django.contrib.auth.models import User

from rest_framework.generics import CreateAPIView, ListCreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from .types import EntryListQuery, HabitListQuery, UserListQuery
from .models import Entry, Habit
from .serializers import EntrySerializer, HabitSerializer, UserSerializer

class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, request, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        user = self.get_object(request, pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class WhoAmIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, request):
        print('\n\n\n', request.user.id, '\n\n\n')
        try:
            return User.objects.get(pk=request.user.id)
        except User.DoesNotExist:
            raise Http404
    
    def get(self, request):
        user = self.get_object(request)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class HabitListCreate(ListCreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        query: HabitListQuery = self.request.GET
        author = query.get("userId")
        return Habit.objects.filter(author=author)

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

class EntryListCreate(ListCreateAPIView):
    serializer_class = EntrySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        query: EntryListQuery = self.request.GET
        
        habitId = query.get("habitId")        
        
        end = query.get("time_end")
        end = datetime.fromisoformat(end) if end else datetime.now()
        
        start = query.get("time_start")
        start = datetime.fromisoformat(start) if start else (end - timedelta(days=7))

        return Entry.objects\
            .filter(habit=habitId)\
            .filter(date__date__range=(start, end))

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