from django.shortcuts import redirect, render,  get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView
from .models import Project, Rating
from users.forms import RatingForm, ProjectCreateForm
from django.contrib import messages
from rest_framework.response import Response
import requests


def search_post(request):
    query = request.GET.get('query')
    if query != None:
        projects = Project.objects.filter(title__contains=query)

    context = {
        'projects': projects,
        'title':'search posts'
    }

    return render(request, 'projects/search.html', context)

def home(request):
    url = 'http://127.0.0.1:8000/api/project-list/'
    res = requests.get(url)
    if (res.status_code == 200):
        response = res.json()
        print(response)
    context = {
        'projects': response
    }
    return render(request, 'projects/home.html', context)

def detail(request,pk):
    url = f'http://127.0.0.1:8000/api/project-detail/{pk}/'
    res = requests.get(url)
    if (res.status_code == 200):
        response = res.json()
        print(response)
    project = Project.objects.get(id=pk)
    ratings = Rating.objects.filter(project=project)
    form = RatingForm()

    rated = False

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=True)
            rating.user = request.user
            rating.project = project
            rating.save()
            messages.success(request, f'You have successfully voted!')
            rated = True
            return redirect('detail', project.id)
        else:
            messages.success(request, f'Failed!')
    else:
        form = RatingForm()

    context = {
        'ratings': ratings,
        'project': response,
        'form' : form,
        'rated': rated
    }

    return render(request, 'projects/detail.html', context)

def delete(request,pk):
    url = f'http://127.0.0.1:8000/api/project-delete/{pk}/'
    res = requests.delete(url)
    print(res)
    messages.success(request, 'project deleted successfully!')
    return redirect('home')

# todo: style rating
# modify readme
# create project classlist for update and creation


class UserPictureListView(ListView):
    model= Project
    template_name='projects/user_projects.html' #<app-name>/<model>_<view-type>.html
    context_object_name='projects'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Project.objects.filter(author=user).order_by('-created')


class ProjectCreateView(LoginRequiredMixin,CreateView):
    model= Project
    fields = ['title', 'description','link', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model= Project
    fields = ['title', 'description','link', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        picture = self.get_object()
        if self.request.user ==  picture.author:
            return True
        return False