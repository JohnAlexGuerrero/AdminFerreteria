from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import TemplateView

class HomeView(LoginRequiredMixin,TemplateView):
    template_name = "home/index.html"
    login_url = 'store:login'

