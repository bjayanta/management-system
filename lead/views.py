from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CreateLeadForm
from .models import Lead

# Create your views here.
class List(LoginRequiredMixin, generic.View):
    def get(self, request):
        leads = Lead.objects.filter(created_by=request.user)

        return render(request, 'lead/list.html', {
            'leads': leads
        })

class Detail(LoginRequiredMixin, generic.View):
    def get(self, request, pk):
        # lead = Lead.objects.filter(created_by=request.user).get(pk=pk)
        lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
        
        return render(request, 'lead/detail.html', {
            'lead': lead
        })

class Delete(LoginRequiredMixin, generic.View):
    def get(self, request, pk):
        lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
        lead.delete()
        
        messages.success(request, 'The lead was deleted.')

        return redirect('lead.list')

class Edit(LoginRequiredMixin, generic.View):
    def get(self, request, pk):
        lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
        form = CreateLeadForm(instance=lead)

        return render(request, 'lead/edit.html', {
            'form': form
        })
    
    def post(self, request, pk):
        lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
        form = CreateLeadForm(request.POST, instance=lead)

        if form.is_valid():
            form.save()

            messages.success(request, 'The changes was saved.')

            return redirect('lead.list')

        form = CreateLeadForm(instance=lead)

        return render(request, 'lead/edit.html', {
            'form': form
        })


class Create(LoginRequiredMixin, generic.View):
    def get(self, request):
        form = CreateLeadForm()
        return render(request, 'lead/create.html', {
            'form': form
        })

    def post(self, request):
        form = CreateLeadForm(request.POST)

        if form.is_valid():
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.save()

            return redirect('lead.list')
        
        return render(request, 'lead/create.html', {
            'form': form
        })