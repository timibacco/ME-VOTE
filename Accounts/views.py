from django.shortcuts import render
from django.views import View
from django.http import HttpRequest
from django.contrib.auth import login,logout
# Create your views here.
class Loggin_view(View):
    def get(self,request, *args, **kwargs):
        return render(request,'login_page.html')
    
class home_view(View):
    def get(self,request, *args, **kwargs):

        return render(request, 'index.html')
    
#class SignMe()
    #signup(Views)
'''class getStarted_view(View):
    def get(self, request, *args, **kwargs):
        return render()'''
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import ElectoralProcess, Participant
from Elections.forms import ParticipantForm

class VoterCreateView(View):
    def get(self, request, link):
        process = get_object_or_404(ElectoralProcess, link=link)
        form = ParticipantForm()
        context = {
            'process': process,
            'form': form
        }
        return render(request, 'voter_create.html', context)

    def post(self, request, link):
        process = get_object_or_404(ElectoralProcess, link=link)
        form = ParticipantForm(request.POST)
        if form.is_valid():
            voter = form.save(commit=False)
            voter.electoral_process = process
            
            voter.save()
            
            return redirect('process_detail', link=process.link)
        context = {
            'process': process,
            'form': form
        }
        return render(request, 'voter_create.html', context)

