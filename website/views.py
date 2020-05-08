from django.shortcuts import render
from .models import ( Slider, Vision, VisionIcons,
                    Gallery, OurCauses, AboutSWLP,AboutSWLPIcons,
                    JoinUs, LeaderSays, LeaderSaysSection, BoardTeam,
                    OurChildrens, OrganizingTeam,BlogSection, Blogs, BlogCitations,
                    OurChildrensSection, AboutUs,Programs
                    )

def index(request,moveToBlogs=None):
    data = {
        'Slider':Slider.objects.all(),
        'Vision':Vision.objects.all(),
        'VisionIcons':VisionIcons.objects.all(),
        'GalleryRow1':Gallery.objects.all()[:4],
        'GalleryRow2':Gallery.objects.all()[4:8],
        'OurCauses':OurCauses.objects.all(),
        'JoinUs':JoinUs.objects.all(),
        'OurChildrensSection':OurChildrensSection.objects.all(),
        'OurChildrens':OurChildrens.objects.all(),
        'BlogSection':BlogSection.objects.all(),
        'Blogs':Blogs.objects.all().order_by('-id')[:3]
    }
    return render(request, 'index.html', data)

def blog_view(request,slug=None):
    blog = Blogs.objects.filter(slug = slug)
    blogCitations = BlogCitations.objects.filter(blog = blog[0])

    if blog:
        data = {'blog':blog[0],'cites':blogCitations}

        return render(request, 'blog.html', data)

    return bloglist(request)

def bloglist(request):
    data = {
        'BlogSection':BlogSection.objects.all(),
        'Blogs':Blogs.objects.all().order_by('-id')
    }
    return render(request, 'bloglist.html', data)

def gallery(request):
    data = {
        'Gallery':Gallery.objects.all()
    }
    return render(request, 'gallery.html', data)


def about(request):
    data = {
        'About':AboutUs.objects.all(),
        'AboutSWLP':AboutSWLP.objects.all(),
        'AboutSWLPIconsRow1':AboutSWLPIcons.objects.all()[:3],
        'AboutSWLPIconsRow2':AboutSWLPIcons.objects.all()[3:],
        'LeaderSaysSection':LeaderSaysSection.objects.all(),
        'LeaderSays':LeaderSays.objects.all(),
        'BoardTeam':BoardTeam.objects.all(),
        'OrganizingTeam':OrganizingTeam.objects.all(),
    }
    return render(request, 'about.html', data)

# def application_form(request):
#     data = {
#         'programs' : Programs.objects.all(),
#     }
#
#     if request.method == "POST":
#         first_name = request.POST.get('first_name')
#         middle_name = request.POST.get('middle_name')
#         last_name = request.POST.get('last_name')
#         phone_no = request.POST.get('phone_no')
#         date_of_birth = request.POST.get('date_of_birth')
#         city_or_town = request.POST.get('city_or_town')
#         state_or_region = request.POST.get('state_or_region')
#         are_you_currently_working = request.POST.get('are_you_currently_working')
#         have_you_been_a_social_worker_before = request.POST.get('have_you_been_a_social_worker_before')
#         academic_qualifications = request.POST.get('academic_qualifications')
#         language_known = request.POST.get('language_known')
#         permanent_address = request.POST.get('permanent_address')
#         email_address = request.POST.get('email_address')
#         when_can_you_start = request.POST.get('when_can_you_start')
#         reference = request.POST.get('reference')
#         additional_info = request.POST.get('additional_info')
#
#         ApplicationForms(first_name=first_name, middle_name=middle_name, last_name = last_name, phone_no=phone_no,
#                         date_of_birth=date_of_birth, city_or_town=city_or_town,state_or_region=state_or_region,
#                         are_you_currently_working=are_you_currently_working, have_you_been_a_social_worker_before=have_you_been_a_social_worker_before,
#                         academic_qualifications=academic_qualifications, language_known=language_known,
#                         permanent_address=permanent_address, email_address=email_address,
#                         when_can_you_start=when_can_you_start,reference=reference,
#                         additional_info=additional_info).save()
#
#         return render(request, '#')
#
#     else:
#         return render(request, '#', data)


def tryy(request):
    return render(request,'try.html', {'a':Programs.objects.all()})
    
def program_view(request,slug=None):
    program = Programs.objects.filter(slug = slug)

    if program:
        data = {'program':program[0]}

        return render(request, 'program.html', data)

    return programlist(request)

def programlist(request):
    data = {
        'Programs':Programs.objects.all().order_by('-id')
    }
    return render(request, 'programlist.html', data)
    