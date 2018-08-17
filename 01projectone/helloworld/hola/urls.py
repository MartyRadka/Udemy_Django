from django.urls import path

from . import views

urlpatterns = [
    # '' if someone goes on homepage, we will be serving this...
    path('', views.homePageViews, name='index'),
]
