from django.shortcuts import render
from .models import ( Slider, Vision, VisionIcons,
                    Gallery, OurCauses, AboutSWLP,AboutSWLPIcons,
                    JoinUs, LeaderSays, LeaderSaysSection, BoardTeam,
                    OurChildrens, OrganizingTeam,BlogSection, Blogs,
                    OurChildrensSection
                    )
# Create your views here.
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

def blog_view(request,id=None):
    blog = Blogs.objects.filter(id = id)

    if blog:
        data = {'blog':blog[0]}

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
        'AboutSWLP':AboutSWLP.objects.all(),
        'AboutSWLPIcons':AboutSWLPIcons.objects.all(),
        'LeaderSaysSection':LeaderSaysSection.objects.all(),
        'LeaderSays':LeaderSays.objects.all(),
        'BoardTeam':BoardTeam.objects.all(),
        'OrganizingTeam':OrganizingTeam.objects.all(),
    }

    return render(request, 'about.html', data)