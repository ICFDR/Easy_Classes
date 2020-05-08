from django.db import models
from datetime import date
from django.utils.text import slugify
from django.dispatch import receiver
import os
from djrichtextfield.models import RichTextField

class AboutUs(models.Model):
    heading = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'About Us'

    def __str__(self):
        return self.heading

class Slider(models.Model):
    heading = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True, default='')
    image = models.ImageField(upload_to='images/slider/', default='')

    class Meta:
        verbose_name_plural = 'Slider'

    def __str__(self):
        return self.heading


class Vision(models.Model):
    heading = models.CharField(max_length=100)
    less = models.TextField(default='')
    more = models.TextField(default='')

    class Meta:
        verbose_name_plural = 'Vision'

    def __str__(self):
        return self.heading


class VisionIcons(models.Model):
    icon = models.CharField(max_length=30)
    icon_name = models.CharField(max_length=50)
    icon_description = models.TextField()
    section = models.ForeignKey(Vision, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Vision Icons'

    def __str__(self):
        return self.icon_name


class Gallery(models.Model):
    image = models.ImageField(upload_to='images/gallery')
    image_alt_txt = models.CharField(max_length=100, blank=True)
    tag = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Gallery'

    def __str__(self):
        return self.tag


class OurCauses(models.Model):
    heading = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/our_causes')
    image_alt_txt = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name_plural = 'Causes'


class AboutSWLP(models.Model):
    heading = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/about_swlp')
    image_alt_txt = models.CharField(max_length=100, blank=True)
    image_heading = models.CharField(max_length=100)
    image_description = models.TextField()
    image_button_text = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'About SWLP'

    def __str__(self):
        return self.heading


class AboutSWLPIcons(models.Model):
    icon = models.CharField(max_length=50)
    icon_text = models.CharField(max_length=50)
    section = models.ForeignKey(AboutSWLP, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'About SWLP Icons'

    def __str__(self):
        return self.icon_text


class JoinUs(models.Model):
    heading = models.CharField(max_length=100)
    description = models.TextField()
    button_text = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Join Us'

    def __str__(self):
        return self.heading


class LeaderSaysSection(models.Model):
    heading = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)

    class Meta:
        verbose_name_plural = 'Leaders Section'

    def __str__(self):
        return self.heading


class LeaderSays(models.Model):
    image = models.ImageField(upload_to='images/leaders/')
    image_alt_txt = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=50)
    about = models.TextField()
    section = models.ForeignKey(LeaderSaysSection, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Leaders'

    def __str__(self):
        return self.name


class BoardTeam(models.Model):
    image = models.ImageField(upload_to='images/board/')
    image_alt_txt = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Board Team'

    def __str__(self):
        return self.name


class OrganizingTeam(models.Model):
    image = models.ImageField(upload_to='images/organizing/')
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    url = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = 'Organizing Team'

    def __str__(self):
        return self.name


@receiver(models.signals.post_delete,sender = OrganizingTeam )
def auto_delete_file_on_delete(sender, instance, **kwargs):

    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


@receiver(models.signals.pre_save,sender = OrganizingTeam)
def auto_delete_file_on_change(sender, instance, **kwargs):

    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).image
    except sender.DoesNOtExist:
        return False

    new_file = instance.image

    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


class OurChildrensSection(models.Model):
    heading = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Children Section'

    def __str__(self):
        return self.heading


class OurChildrens(models.Model):
    image = models.ImageField(upload_to='images/our_childrens/')
    image_alt_txt = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=5000)
    section = models.ForeignKey(OurChildrensSection, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Children'

    def __str__(self):
        return self.name


class BlogSection(models.Model):
    heading = models.CharField(max_length=50)
    description = models.TextField(max_length=5000)

    class Meta:
        verbose_name_plural = 'Blog Section'

    def __str__(self):
        return self.heading


class Blogs(models.Model):
    image = models.ImageField(upload_to='images/blogs/')
    heading = models.CharField(max_length=100)
    content = models.TextField(max_length=5000)
    pub_date = date.today()
    slug = models.SlugField(max_length=100, default='', blank=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.heading, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.heading


class BlogCitations(models.Model):
    url = models.URLField()
    blog = models.ForeignKey(to=Blogs, on_delete=models.CASCADE)

    def __str__(self):
        return self.url

    class Meta:
        verbose_name_plural = 'BlogCitations'

class Programs(models.Model):
    image = models.ImageField(upload_to='images/programs/')
    heading = models.CharField(max_length=100)
    content = RichTextField()
    slug = models.SlugField(max_length=100, default='', blank=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.heading, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Programs'

    def __str__(self):
        return self.heading

class Donate(models.Model):
    image = models.ImageField(upload_to='images/donate/')
    content = RichTextField()
