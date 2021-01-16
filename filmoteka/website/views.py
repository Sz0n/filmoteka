from django.shortcuts import render
from django.views.generic import ListView


# Create your views here.
class HomeView(ListView):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

