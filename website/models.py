from django.db import models
from datetime import datetime


# Create your models here.


class Slider(models.Model) :

    """
    Model for Slider

    """

    heading = models.CharField(max_length = 100)

    description = models.CharField(max_length = 100,blank=True,default='')

    image = models.ImageField(upload_to = 'images/slider/', default='')

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

    tag = models.CharField(max_length = 20)

    class Meta:
        verbose_name_plural = 'Gallery'

    def __str__(self):
        return self.tag


class OurCauses(models.Model):
    heading = models.CharField(max_length = 100)

    description = models.TextField()

    image = models.ImageField(upload_to = 'images/our_causes')


class AboutSWLP(models.Model) :
    heading = models.CharField(max_length = 100)

    description = models.TextField()

    image = models.ImageField(upload_to = 'images/about_swlp')

    image_heading = models.CharField(max_length = 100)

    image_description = models.TextField()

    image_button_text = models.CharField(max_length = 50)

    class Meta:
        verbose_name_plural = 'AboutSWLP'

    def __str__(self):
        return self.heading


class AboutSWLPIcons(models.Model) :
    icon = models.ImageField(upload_to = 'about_swlp/icons/')

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

    name = models.CharField(max_length = 50)

    about = models.TextField()

    section = models.ForeignKey(LeaderSaysSection , on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = 'LeaderSays'

    def __str__(self):
        return self.name


class BoardTeam(models.Model) :
    image = models.ImageField(upload_to = 'images/board/')

    name = models.CharField(max_length = 50)

    role = models.CharField(max_length = 50)

    class Meta:
        verbose_name_plural = 'BoardTeam'

    def __str__(self):
        return self.name


class OrganizingTeam(models.Model) :
    image = models.ImageField(upload_to = 'images/organizing/')

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

    author = models.CharField(max_length = 50)

    role = models.CharField(max_length = 50)

    pub_date = datetime.today()

    content = models.TextField()

    section = models.ForeignKey(BlogSection, on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.author
