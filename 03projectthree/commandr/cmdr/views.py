from django.views.generic import ListView

# fetching data from models
from .models import Cmdr


class HomePageView(ListView):
    model = Cmdr
    template_name = 'index.html'
