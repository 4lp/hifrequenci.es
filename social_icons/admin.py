from django.contrib import admin
from .models import SocialIcon, NetworkChoices

admin.site.register(NetworkChoices)
admin.site.register(SocialIcon)

