from django.shortcuts import render
from django.views import generic

# Create your views here.

class Index(generic.View):
    def get(self, request):
        return render(request, 'core/index.html')


class About(generic.View):
    def get(self, request):
        return render(request, 'core/about.html')