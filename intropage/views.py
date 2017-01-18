from django.shortcuts import render
from django.contrib.staticfiles.templatetags.staticfiles import static

def intro(request):
    image = static('fbi-seizure.jpg')
    return render(request, 'intro.html', {'image':image})
