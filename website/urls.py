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
    path('fellowship',views.fellowship,name = 'fellowship'),
    path('fundraiser', views.fundraiser, name='fundraiser'),
    path('fundraiser/login', views.fundraiser_login, name='fundLogin'),
    path('fundraiser/signup', views.fundraiser_signup, name='fundSignup'),
    path('fundraiser/logout',views.logout_request)
]
