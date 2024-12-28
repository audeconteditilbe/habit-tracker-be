from django.http import HttpRequest, JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Entry, Habit
from .serializers import EntrySerializer, HabitSerializer, UserSerializer

def _list_entries(_request):
    all_entries = Entry.objects.all()
    serialized = EntrySerializer(all_entries, many=True)
    return JsonResponse(serialized.data, safe=False)

def _create_entry(request):
    data = JSONParser().parse(request)
    serialized = EntrySerializer(data=data)
    if serialized.is_valid():
        serialized.save()
        return JsonResponse(serialized.data, status=201)
    return JsonResponse(serialized.errors, status=400)

"""
Generics
"""
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

"""
Mixins
"""
# class HabitListCreate(generics.ListCreateAPIView):
#     serializer_class = HabitSerializer
#     permission_classes = [AllowAny]

#     def get_queryset(self):
#         user = self.request.user
#         return Habit.objects.filter(author=user)

#     def perform_create(self, serializer: HabitSerializer):
#         if serializer.is_valid():
#             serializer.save()
#             # serializer.save(author=self.request.user)
#         else:
#             print(serializer.errors)

"""
class based views
"""
class HabitListCreate(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        habits = Habit.objects.all()
        serializer = HabitSerializer(habits, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = HabitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
function views
"""
@csrf_exempt
def entries_handler(request: HttpRequest):
    if request.method == "GET":
        return _list_entries(request)
    if request.method == "POST":
        return _create_entry(request)
