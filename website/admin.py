from django.contrib import admin
from .models import (Slider, Vision, VisionIcons,
                     Gallery, OurCauses, AboutSWLP, AboutSWLPIcons,
                     JoinUs, LeaderSays, LeaderSaysSection, BoardTeam,
                     OurChildrens, OrganizingTeam, BlogSection, Blogs,
                     OurChildrensSection, AboutUs, Campaign, CampaignBlog,
                     Fellowship, FellowSays, FellowshipImages, online, teacher
                     )

admin.site.register(AboutUs)

admin.site.register(Slider)

admin.site.register(Vision)

admin.site.register(VisionIcons)

admin.site.register(Gallery)

admin.site.register(OurCauses)

admin.site.register(AboutSWLP)

admin.site.register(AboutSWLPIcons)

admin.site.register(JoinUs)

admin.site.register(LeaderSaysSection)

admin.site.register(LeaderSays)

admin.site.register(BoardTeam)

admin.site.register(OrganizingTeam)

admin.site.register(OurChildrensSection)

admin.site.register(OurChildrens)

admin.site.register(BlogSection)

admin.site.register(online)

admin.site.register(teacher)

class InlineCitations(admin.StackedInline):
    model = CampaignBlog
    extra = 1


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    inlines = [InlineCitations, ]


class InlineCitations(admin.StackedInline):
    model = FellowshipImages
    extra = 0
    max_num = 5


class InlineCitations2(admin.StackedInline):
    model = FellowSays
    extra = 0


@admin.register(Fellowship)
class FellowshipAdmin(admin.ModelAdmin):
    inlines = [InlineCitations, InlineCitations2, ]
