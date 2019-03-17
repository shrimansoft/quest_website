from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import clue
import random

def clue_detail(request):
    x=random.randint(1,10)
    context = {
            'number':x,
            'clues':clue.objects.all()
    }
    return render(request, 'clues/clue_view.html', context)
