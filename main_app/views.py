from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import UserForm, InterviewForm
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
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def applications_index(request):
    applications = Application.objects.filter(user=request.user)
    user = request.user
    return render(request, 'applications/index.html', {
        'applications': applications,
        'user': user
    })


class ApplicationCreate(CreateView):
    model = Application
    fields = ['status', 'date_applied', 'title', 'company',
              'description', 'notes', 'salary', 'interest_level']

    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user
        # Let the CreateView do its usual
        return super().form_valid(form)


def interview_index(request, app_id):
    interviews = Interview.objects.filter(application=app_id)
    return render(request, 'interviews/index.html', {
        'application_id': app_id,
        'interviews': interviews
    })


def interview_form(request, app_id):
    return render(request, 'interviews/form.html', {
        'application_id': app_id,
        'interview': InterviewForm
    })

def interview_create(request, app_id):
    form = InterviewForm(request.POST)
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_interview = form.save(commit=False)
        new_interview.application_id = app_id
        new_interview.save()
    # return redirect('interview_index', application_id=app_id)
    return redirect(reverse('interview_index', kwargs={'app_id': app_id}))

