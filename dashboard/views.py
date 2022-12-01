from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import generic

# Create your views here.
class Dashboard(LoginRequiredMixin, generic.View):
    def get(self, request):
        return render(request, 'dashboard/index.html')