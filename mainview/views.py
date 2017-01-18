from django.shortcuts import render, redirect
from soundcloud_songs.views import makePlayer
from news.views import showEntry
from bandcamp_albums.views import makePlayer as bcmakeplayer
from social_icons.views import makeIcons



def mainView(request):
    v1 = showEntry(request)
    v2 = makePlayer(request)
    v3 = bcmakeplayer(request)
    v4 = makeIcons(request)
    return render(request, 'main.html', {'newsentry':v1, 'player':v2, 'bcplayer':v3, 'selected_networks':v4,})


def custom404(request):
    return redirect(mainView)

