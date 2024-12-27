import json
from django.http import HttpRequest, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize

from .models import Entry, Habit
from django.contrib.auth.models import User

# TODO
# auth from fe
# deserialization

@login_required
@csrf_exempt
def habits(request: HttpRequest):
    if request.method == "GET":
        return _list_habits(request)
    if request.method == "POST":
        return _create_habit(request)

def _list_habits(request):
    all_habits = serialize('json', Habit.objects.all())
    return JsonResponse(all_habits, safe=False)

def _create_habit(request: HttpRequest):
    if request.method == 'POST':
        try:
            next_habit = json.loads(request.body)
            author = User.objects.get(id=next_habit.get('author'))
            next_habit = {
                "author": author,
                "name": next_habit.get("name"),
                "description": next_habit.get("description"),
                "goal_frequency": next_habit.get("goal_frequency"),
                "goal_unit": next_habit.get("goal_unit"),
                "goal_type": next_habit.get("goal_type"),
            }
            next_habit = Habit.objects.create(**next_habit)
            return JsonResponse({'message': 'Habit created successfully', 'id': next_habit.id}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)


@login_required
def entries(request):
    all_entries = serialize('json', Entry.objects.all())
    return JsonResponse(all_entries, safe=False)
