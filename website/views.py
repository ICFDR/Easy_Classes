from django.shortcuts import render,redirect
from .models import (Slider, Vision, VisionIcons,
                     Gallery, OurCauses, AboutSWLP, AboutSWLPIcons,
                     JoinUs, LeaderSays, LeaderSaysSection, BoardTeam,
                     OurChildrens, OrganizingTeam, BlogSection, Blogs, BlogCitations,
                     OurChildrensSection, AboutUs, Campaign, Donate, CampaignBlog,Fellowship,FellowSays,FellowshipImages
                     )
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import SignupForm
def index(request, moveToBlogs=None):
    data = {
        'Slider': Slider.objects.all(),
        'Vision': Vision.objects.all(),
        'VisionIcons': VisionIcons.objects.all(),
        'GalleryRow1': Gallery.objects.all()[:4],
        'GalleryRow2': Gallery.objects.all()[4:8],
        'OurCauses': OurCauses.objects.all(),
        'JoinUs': JoinUs.objects.all(),
        'OurChildrensSection': OurChildrensSection.objects.all(),
        'OurChildrens': OurChildrens.objects.all(),
        'BlogSection': BlogSection.objects.all(),
        'Blogs': Blogs.objects.all().order_by('-id')[:3],
        'campaigns': Campaign.objects.all().order_by('-id')[:5],
    }
    return render(request, 'index.html', data)


def blog_view(request, slug=None):
    blog = Blogs.objects.filter(slug=slug)
    blogCitations = BlogCitations.objects.filter(blog=blog[0])

    if blog:
        data = {'blog': blog[0], 'cites': blogCitations,
                'campaigns': Campaign.objects.all().order_by('-id')[:5], }

        return render(request, 'blog.html', data)

    return bloglist(request)


def bloglist(request):
    data = {
        'BlogSection': BlogSection.objects.all(),
        'Blogs': Blogs.objects.all().order_by('-id'),
        'campaigns': Campaign.objects.all().order_by('-id')[:5]
    }
    return render(request, 'bloglist.html', data)


def gallery(request):
    data = {
        'Gallery': Gallery.objects.all(),
        'campaigns': Campaign.objects.all().order_by('-id')[:5]
    }
    return render(request, 'gallery.html', data)


def about(request):
    data = {
        'About': AboutUs.objects.all(),
        'AboutSWLP': AboutSWLP.objects.all(),
        'AboutSWLPIconsRow1': AboutSWLPIcons.objects.all()[:3],
        'AboutSWLPIconsRow2': AboutSWLPIcons.objects.all()[3:],
        'LeaderSaysSection': LeaderSaysSection.objects.all(),
        'LeaderSays': LeaderSays.objects.all(),
        'BoardTeam': BoardTeam.objects.all(),
        'OrganizingTeam': OrganizingTeam.objects.all(),
        'campaigns': Campaign.objects.all().order_by('-id')[:5],
    }
    return render(request, 'about.html', data)


def campaign_view(request, slug=None):
    campaign = Campaign.objects.filter(slug=slug)
    blog = CampaignBlog.objects.filter(blog=campaign[0])

    if campaign:
        data = {'campaign': campaign[0],
                'blog': blog,
                'campaigns': Campaign.objects.all().order_by('-id')[:5], }

        return render(request, 'campaign.html', data)

    return campaignlist(request)


def campaignlist(request):
    data = {
        'campaigns': Campaign.objects.all().order_by('-id')
    }
    return render(request, 'campaignlist.html', data)


def donate(request):
    data = {
        'donate': Donate.objects.all()[0],
        'campaigns': Campaign.objects.all().order_by('-id')[:5],
    }
    return render(request, 'donate.html', data)


def fellowship(request):
    data = {
        'fellowship':Fellowship.objects.all()[0],
        'campaigns': Campaign.objects.all().order_by('-id')[:5],
    }

    return render(request, 'fellowship.html',data)



def fundraiser(request):
    if(request.user.is_authenticated):
        return render(request, 'fundraiser.html')
    return render(request, 'LoginSignup.html')


def fundraiser_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('fundraiser')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request,
                  template_name="fundLogin.html",
                  context={"form": form})


def fundraiser_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            email=form.cleaned_data.get('email')
            password=form.cleaned_data.get('password')
            user=authenticate(username=email,password=password)
            login(request,user)
            messages.success(request,f'sign up successful')
            return redirect('fundraiser')
        else:
            messages.success(request, f'give valid inputs')
            return redirect('fundSignup')
    form = SignupForm()
    return render(request,'fundSignup.html',{'form':form})


def logout_request(request):
    logout(request)
    return redirect("fundraiser")