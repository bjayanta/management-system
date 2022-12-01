from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import generic

from .models import Account

# Create your views here.
class Signup(generic.View):
    form = UserCreationForm()

    def get(self, request):
        return render(request, 'account/signup.html', {
            'form': self.form
        })
    
    def post(self, request):
        self.form = UserCreationForm(request.POST)

        if self.form.is_valid():
            user = self.form.save()
            
            Account.objects.create(user=user)

            return redirect('/sign-in/')

        return render(request, 'account/signup.html', {
            'form': self.form
        })
        

