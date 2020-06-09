from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import UserForm, UserProfileForm
from django.contrib.auth.models import User
from .models import UserProfile
# Create your views here.

class Register(TemplateView):
    template_name = "fundraiser/register.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['UserForm'] = UserForm()
        context['UserProfileForm'] = UserProfileForm()
        context['registered'] = False
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        user_form = UserForm(request.POST)
        user_profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and user_profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_profile = user_profile_form.save(commit = False)
            user_profile.user = user

            if 'profile_pic' in request.FILES:
                user_profile.profile_pic = request.FILES['profile_pic']

            user_profile.save()
            context['registered'] = True
            print('user registered')
        return self.render_to_response(context)