from django.shortcuts import render
from link.models import Link


def index(request):
    links = Link.objects.all()
    return render(request, 'core/index.html',{'links':links})