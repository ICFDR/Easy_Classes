from django.contrib import admin
from django.contrib.auth.models import Group

admin.site.site_header = "iCFDR Admin"
admin.site.site_title = "iCFDR Admin Portal"
admin.site.index_title = "Welcome to iCFDR Administration Portal"
admin.site.unregister(Group)