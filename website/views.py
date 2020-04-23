from django.shortcuts import render
from .models import ( Slider, Vision, VisionIcons,
                    Gallery, OurCauses, AboutSWLP,AboutSWLPIcons,
                    JoinUs, LeaderSays, LeaderSaysSection, BoardTeam,
                    OurChildrens, OrganizingTeam,BlogSection, Blogs,
                    OurChildrensSection
                    )
# Create your views here.
def index(request):

    data = {
        'Slider':Slider.objects.all(),
        'Vision':Vision.objects.all(),
        'VisionIcons':VisionIcons.objects.all(),
        'Gallery':Gallery.objects.all().order_by('-id')[:8],
        'OurCauses':OurCauses.objects.all(),
        'AboutSWLP':AboutSWLP.objects.all(),
        'AboutSWLPIcons':AboutSWLPIcons.objects.all(),
        'JoinUs':JoinUs.objects.all(),
        'LeaderSaysSection':LeaderSaysSection.objects.all(),
        'LeaderSays':LeaderSays.objects.all(),
        'BoardTeam':BoardTeam.objects.all(),
        'OrganizingTeam':OrganizingTeam.objects.all(),
        'OurChildrensSection':OurChildrensSection.objects.all(),
        'OurChildrens':OurChildrens.objects.all(),
        'BlogSection':BlogSection.objects.all(),
        'Blogs':Blogs.objects.all(),

    }

    return render(request, 'index.html', data)


def blog_view(request,id):

    data = {'blog':Blogs.objects.filter(id = id)[0]}
    print(data['blog'])

    return render(request, 'blog.html', data)
