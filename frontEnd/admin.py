from django.contrib import admin
from .models import PageText

# style stuff
admin.site.site_header = "Content Authoring"
admin.site.site_title = "Content Authoring"


admin.site.register(PageText)