from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Subscriber, Image, Location, Category, Comments, Profile
from .forms import SubscribeForm, NewPostForm, CommentForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
import datetime as dt
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    title = 'Home'
    current_user = request.user

    
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
            image = form.save(commit=False)
            image.poster = current_user
            image.save()
        return redirect('index')

    else:
        form = NewPostForm()
    return render(request, 'registration/new_post.html', {"form": form})

@login_required(login_url='/accounts/login/')
def search_projects(request):
    if 'image' in request.GET and request.GET["project"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_images(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "projects": searched_projects})

    else:
        message = "You haven't searched for any person"
        return render(request, 'search.html', {"message": message})
    
def single_post(request, id):

    try:
        image = Image.objects.get(pk=id)

    except DoesNotExist:
        raise Http404()

    current_user = request.user
    comments = Comments.get_comment(Comments, id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment']

            commentt = Comments()
            commentt.image = image
            commentt.user = current_user
            commentt.comment = comment
            commentt.save()

    else:
        form = CommentForm()

    return render(request, 'single.html', {"image": image,'form': form,'comments': comments})