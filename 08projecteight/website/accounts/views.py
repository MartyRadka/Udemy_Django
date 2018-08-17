from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class SignUpView(generic.CreateView):
    form_class = UserCreationForm  # creation of user Form
    success_url = reverse_lazy('login')  # the success url if the user was created.
    # this will redirect user to login page, but we use reverse_lazy, cause thanks that
    # it will be redirected after the creation of the user form and it's authetication,
    # so after the whole process, not in the same time as creation.
    template_name = 'signup.html'
