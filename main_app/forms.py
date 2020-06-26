from django.forms import ModelForm
from .models import User, Interview


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]


class InterviewForm(ModelForm):
    class Meta:
        model = Interview
        fields = ["company_info", "preparation_text", "questions", "rating"]
