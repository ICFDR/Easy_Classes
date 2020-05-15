from django.shortcuts import render
from .models import (Slider, Vision, VisionIcons,
                     Gallery, OurCauses, AboutSWLP, AboutSWLPIcons,
                     JoinUs, LeaderSays, LeaderSaysSection, BoardTeam,
                     OurChildrens, OrganizingTeam, BlogSection, Blogs, BlogCitations,
                     OurChildrensSection, AboutUs, Campaign, Donate, CampaignBlog
                     )


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
