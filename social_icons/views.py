from django.shortcuts import render
from social_icons.models import SocialIcon

def makeIcons(request):
    networks = SocialIcon.objects.filter(isSelected=True)
    return networks
