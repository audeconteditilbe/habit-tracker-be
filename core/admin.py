from django.contrib import admin
from .models import Habit, Entry


# Hide private habits from admin page
@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(private=False)


admin.site.register(Entry)
