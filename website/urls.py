from django.contrib import admin
from django.urls import path, include
from . import views
from .views import redirect_view

urlpatterns = [
    path('', views.index,name = 'home'),
    path('blogs/<slug:slug>',views.blog_view,name = 'blog'),
    path('blogs',views.bloglist,name = 'bloglist'),
    path('children',views.children,name = 'children'),
    path('about',views.about,name = 'about'),
    path('campaigns/<slug:slug>',views.campaign_view,name = 'campaign'),
    path('donate',views.donate,name = 'donate'),
    path('fellowship',views.fellowship,name = 'fellowship'),
    path('online',views.online, name = 'online'),
    path('blogs/', redirect_view),

]
