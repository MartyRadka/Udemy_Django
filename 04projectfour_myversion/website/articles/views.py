from django.views.generic import ListView, DetailView, TemplateView

from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'index.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail.html'
    context_object_name = 'batman'


class ContactPageView(TemplateView):
    template_name = 'contact.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class HomePageView(TemplateView):
    template_name = 'base.html'
