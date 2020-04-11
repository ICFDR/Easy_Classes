from django.contrib import admin
from .models import Slider, Vision, Vision_icons, Events, \
    All_events, Children_events, Empowerment_events, Environment_events,\
    Health_events, Elderly_events, About_SWLP, About_SWLP_icons, \
    Join_us, Leader_says_section, Leader_says, Board_team, \
    Organizing_team, Our_childrens_section, Our_childrens, Blog_section,\
    Blogs
# Register your models here.

admin.site.register(Slider)

admin.site.register(Vision)

admin.site.register(Vision_icons)

admin.site.register(Events)

admin.site.register(All_events)

admin.site.register(Children_events)

admin.site.register(Empowerment_events)

admin.site.register(Environment_events)

admin.site.register(Health_events)

admin.site.register(Elderly_events)

admin.site.register(About_SWLP)

admin.site.register(About_SWLP_icons)

admin.site.register(Join_us)

admin.site.register(Leader_says_section)

admin.site.register(Leader_says)

admin.site.register(Board_team)

admin.site.register(Organizing_team)

admin.site.register(Our_childrens_section)

admin.site.register(Our_childrens)

admin.site.register(Blog_section)

admin.site.register(Blogs)
