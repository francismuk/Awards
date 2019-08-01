from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Subscriber, Image, Location, Category, Comments, Profile
from .forms import SubscribeForm, NewPostForm, CommentForm
from .email import send_welcome_email

# Create your views here.

def index(request):
    title = 'Home'
    current_user = request.user

    if request.GET.get('location'):
        images = Image.filter_by_location(request.GET.get('location'))

    else:
        images = Image.objects.all()

    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            recipient = Subscriber(name=name, email=email)
            recipient.save()
            send_welcome_email(name, email)
            HttpResponseRedirect('index', {"name": name})

    else:
        form = SubscribeForm()

    return render(request, 'index.html', {'title': title, 'images': images, 'letterForm': form})