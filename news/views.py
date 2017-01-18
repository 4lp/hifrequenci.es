from news.models import Entry
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.http import Http404

def showEntry(request):
    if request.is_ajax():
        allentries = Entry.objects.all()
        ordentries = allentries.order_by("-date")
        entriesLoaded = request.session.get('entries_loaded')
        entriesLoadedp2 = entriesLoaded + 2
        entries = ordentries[entriesLoaded:entriesLoadedp2]
        data = render_to_string('news.html', {'newsentry': entries})
        request.session['entries_loaded'] += 2
        return HttpResponse(data)
    else:
        request.session['entries_loaded'] = 2
        allentries = Entry.objects.all()
        ordentries = allentries.order_by("-date")
        entries = ordentries[:2]
        return entries

def lessEntries(request):
    if request.is_ajax():
        request.session['entries_loaded'] = 2
        allentries = Entry.objects.all()
        ordentries = allentries.order_by("-date")
        entries = ordentries[:2]
        data = render_to_string('news.html', {'newsentry': entries})
        return HttpResponse(data)
    else:
        raise Http404