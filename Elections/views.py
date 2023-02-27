
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import ElectoralProcess
from Accounts.models import Participant
from django.utils.timezone import datetime
from Elections.views import ElectoralProcess
from .forms import ElectoralProcessForm, forms

class ProcessDetailView(View):
    def get(self, request, link):
        process = get_object_or_404(ElectoralProcess, link=link)
        voters = process.voter_set.all()
        context = {
            'process': process,
            'voters': voters
        }
        return render(request, 'process_detail.html', context)
 

class ElectionCreateView(View):
    def post(self,request,link):
        if request.method == 'POST':
            # Get the date and time values from the POST data
            
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
           
            name  = request.POST.get('name')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            no_of_voters = request.POST.get('number of voters')
            # Get the date and time values from the POST data
#           start_date_str = request.POST.get('start_date')
   #         start_time_str = request.POST.get('start_time')
  #          end_date_str = request.POST.get('end_date')
 #           end_time_str = request.POST.get('end_time')
#
#
     #       # Convert the date and time strings to datetime objects
    #        startDate_obj = datetime.strptime(start_date_str, '%Y-%m-%d').date()
   #         startTime_obj = datetime.strptime(start_time_str, '%H:%M').time()
  #          endDate_obj = datetime.strptime(end_date_str, '%Y-%m-%d').date()
 #           endTime_obj = datetime.strptime(end_time_str, '%H:%M').time()
#
   #         # Combine the date and time objects into a datetime object
  #          startDatetime_obj = datetime.combine(startDate_obj, startTime_obj)
 #           endDatetime_obj = datetime.combine(endDate_obj,endTime_obj)

     #       # Create a new instance of your model and save it
    #        my_model = ElectoralProcess(
   #             start_time=startDatetime_obj,
  #              end_time=endDatetime_obj,
 #               name = name,
 #               no_of_voters = no_of_voters
 #               )
 #           my_model.save()
            
            form = ElectoralProcessForm(request.POST)
            process = get_object_or_404(ElectoralProcess, link=link)
            if form.is_valid():
                if password1 == password2 :
                    election = form.save(password = password2,
                                        first_name = first_name,
                                        )
                    election = form.save(commit=False)
                    election.electoral_process = process
                    
                    election.save()
                else:
                    forms.ValidationError.messages({Exception})
                
                return redirect('process_detail', link=process.link)
            context = {
                'process': process,
                'form': form
            }
            # Redirect the user to a success page
        
            return redirect('success')
        else:

    # Render a template with a form for the user to enter the date and time
            return render(request, 'create_election.html',context)


  
       
        

        