from django.db import models
from datetime import date
from django.utils.text import slugify

class Slider(models.Model) :
    heading = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100,blank=True,default='')
    image = models.ImageField(upload_to = 'images/slider/', default='')
    image_alt_txt = models.CharField(max_length= 100, blank= True)

    class Meta:
        verbose_name_plural = 'Slider'
    def __str__(self):
        return self.heading

class Vision(models.Model) :
    heading = models.CharField(max_length = 100)
    less = models.TextField(default='')
    more = models.TextField(default='')

    class Meta:
        verbose_name_plural = 'Vision'
    def __str__(self):
        return self.heading

class VisionIcons(models.Model):
    icon = models.CharField(max_length = 30)
    icon_name = models.CharField(max_length = 50)
    icon_description = models.TextField()
    section = models.ForeignKey(Vision, on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = 'VisionIcons'
    def __str__(self):
        return self.icon_name

class Gallery(models.Model) :
    image = models.ImageField(upload_to = 'images/gallery')
    image_alt_txt = models.CharField(max_length=100, blank=True)
    tag = models.CharField(max_length = 20)

    class Meta:
        verbose_name_plural = 'Gallery'
    def __str__(self):
        return self.tag

class OurCauses(models.Model):
    heading = models.CharField(max_length = 100)
    description = models.TextField()
    image = models.ImageField(upload_to = 'images/our_causes')
    image_alt_txt = models.CharField(max_length=100, blank=True)
	
    class Meta:
        verbose_name_plural = 'Causes'

class AboutSWLP(models.Model) :
    heading = models.CharField(max_length = 100)
    description = models.TextField()
    image = models.ImageField(upload_to = 'images/about_swlp')
    image_alt_txt = models.CharField(max_length=100, blank=True)
    image_heading = models.CharField(max_length = 100)
    image_description = models.TextField()
    image_button_text = models.CharField(max_length = 50)

    class Meta:
        verbose_name_plural = 'AboutSWLP'
    def __str__(self):
        return self.heading

class AboutSWLPIcons(models.Model) :
    icon = models.ImageField(upload_to = 'about_swlp/icons/')
    image_alt_txt = models.CharField(max_length=100, blank=True)
    icon_text = models.CharField(max_length = 50)
    section = models.ForeignKey(AboutSWLP , on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = 'AboutSWLPIcons'
    def __str__(self):
        return self.icon_text

class JoinUs(models.Model) :
    heading = models.CharField(max_length = 100)
    description = models.TextField()
    button_text = models.CharField(max_length = 50)

    class Meta:
        verbose_name_plural = 'JoinUs'
    def __str__(self):
        return self.heading

class LeaderSaysSection(models.Model) :
    heading = models.CharField(max_length = 100)
    description = models.CharField(max_length = 5000)

    class Meta:
        verbose_name_plural = 'LeaderSaysSection'
    def __str__(self):
        return self.heading

class LeaderSays(models.Model) :
    image = models.ImageField(upload_to = 'images/leaders/')
    image_alt_txt = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length = 50)
    about = models.TextField()
    section = models.ForeignKey(LeaderSaysSection , on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = 'LeaderSays'
    def __str__(self):
        return self.name

class BoardTeam(models.Model) :
    image = models.ImageField(upload_to = 'images/board/')
    image_alt_txt = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length = 50)
    role = models.CharField(max_length = 50)

    class Meta:
        verbose_name_plural = 'BoardTeam'
    def __str__(self):
        return self.name

class OrganizingTeam(models.Model) :
    image = models.ImageField(upload_to = 'images/organizing/')
    image_alt_txt = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length = 50)
    role = models.CharField(max_length = 50)

    class Meta:
        verbose_name_plural = 'OrganizingTeam'
    def __str__(self):
        return self.name

class OurChildrensSection(models.Model) :
    heading = models.CharField(max_length = 50)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'OurChildrensSection'
    def __str__(self):
        return self.heading

class OurChildrens(models.Model) :
    image = models.ImageField(upload_to = 'images/our_childrens/')
    image_alt_txt = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 5000)
    section = models.ForeignKey(OurChildrensSection , on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = 'OurChildrens'
    def __str__(self):
        return self.name

class BlogSection(models.Model) :
    heading = models.CharField(max_length = 50)
    description = models.TextField(max_length = 5000)

    class Meta:
        verbose_name_plural = 'BlogSection'
    def __str__(self):
        return self.heading

class Blogs(models.Model) :
    image = models.ImageField(upload_to = 'images/blogs/')
    image_alt_txt = models.CharField(max_length=100, blank=True)
    heading = models.CharField(max_length = 100,default='Blog Heading goes here ')
    summary = models.TextField(max_length = 150,default='Blog Summary goes here')
    content = models.TextField(max_length = 5000,default='Blog Content goes here')
    author = models.CharField(max_length = 50)
    pub_date = date.today()
    slug = models.SlugField(default='', blank = True, unique = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.heading, allow_unicode = True)
        super().save(*args, **kwargs)
    class Meta:
        verbose_name_plural = 'Blogs'
    def __str__(self):
        return self.author