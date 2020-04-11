from django.db import models


# Create your models here.


class Slider(models.Model) :
    heading = models.CharField(max_length = 100)

    description = models.CharField(max_length = 5000)

    image = models.ImageField(upload_to = 'slider/')

    button_text = models.CharField(max_length = 50)


class Vision(models.Model) :
    heading = models.CharField(max_length = 100)

    description = models.CharField(max_length = 5000)

    icon = models.ImageField(upload_to = 'vision-icons/')

    icon_name = models.CharField(max_length = 50)

    icon_description = models.CharField(max_length = 2000)


class Events(models.Model) :
    heading = models.CharField(max_length = 100)

    description = models.CharField(max_length = 5000)


class Children_events(models.Model) :
    image = models.ImageField(upload_to = 'events/child/')

    event = models.ForeignKey(Events , on_delete = models.CASCADE)


class All_events(models.Model) :
    image = models.ImageField(upload_to = 'events/all/')

    event = models.ForeignKey(Events , on_delete = models.CASCADE)


class Empowerment_events(models.Model) :
    image = models.ImageField(upload_to = 'events/emp/')

    event = models.ForeignKey(Events , on_delete = models.CASCADE)


class Health_events(models.Model) :
    image = models.ImageField(upload_to = 'events/health/')

    event = models.ForeignKey(Events , on_delete = models.CASCADE)


class Environment_events(models.Model) :
    image = models.ImageField(upload_to = 'events/env/')

    event = models.ForeignKey(Events , on_delete = models.CASCADE)


class Elderly_events(models.Model) :
    image = models.ImageField(upload_to = 'events/elderly/')

    event = models.ForeignKey(Events , on_delete = models.CASCADE)


class About_SWLP(models.Model) :
    heading = models.CharField(max_length = 100)

    description = models.CharField(max_length = 5000)

    image = models.ImageField(upload_to = 'about_swlp/image')

    image_heading = models.CharField(max_length = 100)

    image_description = models.CharField(max_length = 2000)

    image_button_text = models.CharField(max_length = 50)


class About_SWLP_icons(models.Model) :
    icon = models.ImageField(upload_to = 'about_swlp/icons/')

    icon_text = models.CharField(max_length = 50)

    about = models.ForeignKey(About_SWLP , on_delete = models.CASCADE)


class Join_us(models.Model) :
    heading = models.CharField(max_length = 100)

    description = models.CharField(max_length = 5000)

    button_text = models.CharField(max_length = 50)


class Leader_says_section(models.Model) :
    heading = models.CharField(max_length = 100)

    description = models.CharField(max_length = 5000)


class Leader_says(models.Model) :
    image = models.ImageField(upload_to = 'leaders/')

    name = models.CharField(max_length = 50)

    about = models.CharField(max_length = 5000)

    leader_says_section = models.ForeignKey(Leader_says_section , on_delete = models.CASCADE)


class Board_team(models.Model) :
    image = models.ImageField(upload_to = 'board/')

    name = models.CharField(max_length = 50)

    role = models.CharField(max_length = 50)


class Organizing_team(models.Model) :
    image = models.ImageField(upload_to = 'organizing/')

    name = models.CharField(max_length = 50)

    role = models.CharField(max_length = 50)
