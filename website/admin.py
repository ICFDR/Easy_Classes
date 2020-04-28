from django.contrib import admin
from .models import ( Slider, Vision, VisionIcons,
                    Gallery, OurCauses, AboutSWLP,AboutSWLPIcons,
                    JoinUs, LeaderSays, LeaderSaysSection, BoardTeam,
                    OurChildrens, OrganizingTeam,BlogSection, Blogs,
                    OurChildrensSection, BlogCitations,
                    )


# Register your models here.

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

class InlineCitations(admin.StackedInline):
    model = BlogCitations
    extra = 1

@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
   inlines = [InlineCitations,]
