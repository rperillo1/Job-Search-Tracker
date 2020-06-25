from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserForm, InterviewForm
from .models import Application, Skills, Interview


def home(request):
    user_form = UserForm()
    return render(request, "home.html", {"user_form": user_form})


def signup(request):
    error_message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            error_message = "Invalid sign up - try again"
    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "registration/signup.html", context)


@login_required
def applications_index(request):
    applications = Application.objects.filter(user=request.user).order_by(
        "-interest_level"
    )
    user = request.user

    return render(
        request,
        "applications/index.html",
        {"applications": applications, "user": user,},
    )


class ApplicationShow(DetailView, LoginRequiredMixin):
    model = Application


class ApplicationCreate(CreateView, LoginRequiredMixin):
    model = Application
    fields = [
        "status",
        "date_applied",
        "title",
        "company",
        "description",
        "notes",
        "salary",
        "interest_level",
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ApplicationDelete(DeleteView, LoginRequiredMixin):
    model = Application
    success_url = "/applications/"


class ApplicationUpdate(UpdateView, LoginRequiredMixin):
    model = Application
    fields = [
        "status",
        "title",
        "date_applied",
        "salary",
        "interest_level",
        "description",
        "notes",
    ]


@login_required
def interview_index(request, app_id):
    interviews = Interview.objects.filter(application=app_id)
    return render(
        request,
        "interviews/index.html",
        {"application_id": app_id, "interviews": interviews,},
    )


@login_required
def interview_form(request, app_id):
    return render(
        request,
        "interviews/form.html",
        {"application_id": app_id, "interview": InterviewForm},
    )


@login_required
def interview_create(request, app_id):
    form = InterviewForm(request.POST)
    if form.is_valid():
        new_interview = form.save(commit=False)
        new_interview.application_id = app_id
        new_interview.save()
    return redirect(reverse("interview_index", kwargs={"app_id": app_id}))


class InterviewShow(DetailView, LoginRequiredMixin):
    model = Interview


class InterviewDelete(DeleteView, LoginRequiredMixin):
    model = Interview

    def get_success_url(self):
        return reverse(
            "interview_index", kwargs={"app_id": self.kwargs["application_pk"]}
        )


class InterviewUpdate(UpdateView, LoginRequiredMixin):
    model = Interview
    fields = ["company_info", "preparation_text", "questions", "rating"]

    def get_success_url(self):
        print("self kwargs", self.kwargs)
        return reverse(
            "interview_detail",
            kwargs={
                "application_pk": self.kwargs["application_pk"],
                "pk": self.kwargs["pk"],
            },
        )
