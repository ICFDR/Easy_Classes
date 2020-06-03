from django.shortcuts import render,redirect
from .models import (Slider, Vision, VisionIcons,
                     Gallery, OurCauses, AboutSWLP, AboutSWLPIcons,
                     JoinUs, LeaderSays, LeaderSaysSection, BoardTeam,
                     OurChildrens, OrganizingTeam, BlogSection, Blogs, BlogCitations,
                     OurChildrensSection, AboutUs, Campaign, Donate, CampaignBlog,Fellowship,FellowSays,FellowshipImages,
FellowshipApplicationForm
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
        'images':FellowshipImages.objects.filter(fellowship=Fellowship.objects.all()[0]),
        'fellow_says':FellowSays.objects.filter(fellowship=Fellowship.objects.all()[0]),
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


def fellowship_application(request):
    data = {
        'campaigns': Campaign.objects.all().order_by('-id')[:5],
    }

    if request.method == "POST":
        FellowshipApplicationForm(
            full_name=request.POST.get('name'),
            email=request.POST.get('email'),
            mobile_no = request.POST.get('mob'),
            sex = request.POST.get('sex'),
            d_o_b = request.POST.get('date'),
            city = request.POST.get('city'),
            state = request.POST.get('state'),
            permanent_address = request.POST.get('address'),
            academic_qualification = request.POST.get('academic'),
            language_known = request.POST.get('lang'),
            are_you_currently_working = request.POST.get('working'),
            if_yes_please_mention_the_organisations = request.POST.get('org'),
            have_you_been_a_social_worker_before = request.POST.get('before'),
            if_yes_please_mention_the_organisation = request.POST.get('b_org'),
            define_leadership = request.POST.get('leadership'),
            why_do_you_want_to_be_a_fellow = request.POST.get('why_fellow'),
            why_do_you_think_education_is_important = request.POST.get('edu_imp'),
            how_can_you_change_the_perspective_of_a_chld_who_think_educartion_is_worthless = request.POST.get('edu_worth'),
            explain_how_you_are_going_to_be_empathetic_with_the_child_who_are_divergent = request.POST.get('empathetic'),
            what_are_your_strength_and_weakness_as_a_social_worker = request.POST.get('strengths'),
            what_motivates_you_to_selfilessly_work_for_us_without_pay = request.POST.get('motivates'),
            how_do_you_plan_on_building_a_healthy_relationship_with_the_students = request.POST.get('healthy'),
            when_you_start = request.POST.get('start'),
            references = request.POST.get('references'),
        ).save()

        return render(request, 'thanks.html',data)
    else:

        return render(request, 'fellowship_application.html',data)