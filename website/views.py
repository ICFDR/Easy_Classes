from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):

    data = {
        'Slider':Slider.objects.all(),
        'SliderImage':SliderImage.objects.all(),
        'Vision':Vision.objects.all(),
        'VisionIcons':VisionIcons.objects.all(),
        'Events':Events.objects.all(),
        'ChildrenEvents':ChildrenEvents.objects.all(),
        'EmpowermentEvents':EmpowermentEvents.objects.all(),
        'HealthEvents':HealthEvents.objects.all(),
        'EnvironmentEvents':ElderlyEvents.objects.all(),
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

    return render(request, 'test.html', data)
