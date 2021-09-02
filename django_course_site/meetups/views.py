from django.shortcuts import render
from django.http import HttpResponse

from .models import Meetup
from .forms import RegistrationForm

# Create your views here.

def index(request):
    meetups = Meetup.objects.all()

    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups
    })

def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        registrarion_form = RegistrationForm()
        return render(request, 'meetups/meetup-details.html', {
            'meetup_title': selected_meetup.title,
            'meetup': selected_meetup,
            'form': registrarion_form
        })
    except Exception as e:
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False
        })