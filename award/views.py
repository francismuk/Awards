from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Subscriber, Image, Location, Category, Comments, Profile
from .forms import SubscribeForm, NewPostForm, CommentForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required

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

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.poster = current_user
            post.save()
        return redirect('index')

    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})

def search_projects(request):
    if 'image' in request.GET and request.GET["project"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_images(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "projects": searched_projects})

    else:
        message = "You haven't searched for any person"
        return render(request, 'search.html', {"message": message})