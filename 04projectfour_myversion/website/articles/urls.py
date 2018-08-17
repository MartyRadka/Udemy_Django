from django.urls import path

from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='index'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article_page'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('contact/', views.ContactPageView.as_view(), name='contact'),
]
