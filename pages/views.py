from django.shortcuts import render
from django.views.generic import ListView

from users.models import CustomUser


class HomepageView(ListView):
    template_name = 'home.html'
    model = CustomUser
