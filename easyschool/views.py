from django.shortcuts import render
from headlines.models import Headline


def index(request):
    Content = Headline.objects.all()
    return render(request, 'index.html', {'content': Content})