from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .models import Candidate, Position, Vote
# Create your views here.
def index(request):
    context = {}
    candidates = Candidate.objects.all()
    context['candidates'] = candidates[::-1]
    return render(request, "index.html", context)
