from django.db import models
from datetime import date
from django.utils.text import slugify

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
    summary = models.TextField(max_length=150)
    content = models.TextField(max_length=5000)
    pub_date = date.today()
    slug = models.SlugField(default='', blank=True, unique=True)

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

    why_be_a_fellow_content = models.TextField()
    about_the_fellowship_content = models.TextField()
    the_pre_eminent_will_be_awarded_content = models.TextField()
    eligibility_content = models.TextField()
    selection_Process_content = models.TextField()

    def __str__(self):
        return self.why_be_a_fellow_content


class ApplicationForm(models.Model):

    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=12)
    date_of_birth = models.CharField(max_length=20)
    city_or_town = models.CharField(max_length=50)
    state_or_region = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    are_you_currently_working = models.CharField(max_length=20)
    have_you_been_a_social_worker_before = models.CharField(max_length=100)
    academic_qualifications = models.CharField(max_length=50)
    language_known = models.CharField(max_length=100)
    permanent_address = models.TextField(max_length=100)
    email_address = models.EmailField()
    # define_leadership = models.TextField()
    # why_do_want_to_be_a_fellow = models.TextField()
    # why_do_you_think_education_is_important = models.TextField()
    # change_tyhe = models.TextField()
    # why_do_want_to_be_a_fellow = models.TextField()
    when_can_you_start = models.CharField(max_length=30)
    reference = models.CharField(max_length=50)
    additional_info = models.TextField(blank=True)


    def __str__(self):
        return self.first_name









