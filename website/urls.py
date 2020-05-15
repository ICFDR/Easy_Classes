from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.index,name = 'home'),
    path('blogs/<slug:slug>',views.blog_view,name = 'blog'),
    path('blogs',views.bloglist,name = 'bloglist'),
    path('gallery',views.gallery,name = 'gallery'),
    path('about',views.about,name = 'about'),
    path('campaigns/<slug:slug>',views.campaign_view,name = 'campaign'),
    path('donate',views.donate,name = 'donate'),
]
