from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.contrib import messages

from .forms import GuestForm
from .models import Guests, Countdown
def index(request):
    template = loader.get_template("landing_page/index.html")
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            guests = form.cleaned_data['guests']
            message = form.cleaned_data['message']
            Guests.objects.create(name=name,number_of_guests=guests, message=message)
            # messages.add_message(request, messages.INFO, "You have successfully registered!")
            messages.error(request,'Thank you! You have been registered!')
            return HttpResponseRedirect('/landing_page/')
    else:
        form = GuestForm()
    context = {
        "form": form,
    }
    return HttpResponse(template.render(context,request))
    # return render(request,template,context)

def jaya(request):
  ob=Countdown.objects.get(id=2)
  return render(request,'index.html',{'ob':ob})