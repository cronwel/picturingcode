from django.urls import path, re_path
from .import views

app_name = 'articles'
# app_name = 'articles' is a name spacing technique

urlpatterns = [
    path('', views.articles_list, name="list"),
    path('create/', views.article_create, name='create'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.article_details, name="details"),
]

