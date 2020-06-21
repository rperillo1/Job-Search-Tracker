from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import UserForm
from .models import Application, Skills, Interview
# Create your views here.


def home(request):
    user_form = UserForm()
    return render(request, 'home.html', {
        'user_form': user_form
    })

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def applications_index(request):
    applications = Application.objects.all()
    return render(request, 'applications/index.html', {
        'applications': applications
    })


class ApplicationCreate(CreateView):
    model = Application
    fields = '__all__'