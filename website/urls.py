from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.index,name = 'home'),
    path('blogs/<int:id>',views.blog_view,name = 'blog'),
    path('blogs',views.blog_view,name = 'allBlogs'),
]
