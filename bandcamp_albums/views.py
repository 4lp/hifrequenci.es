from django.shortcuts import render
from bandcamp_albums.models import BCAlbum

def makePlayer(request):
    albums = BCAlbum.objects.all()
    html = ""
    for album in albums:
        if album.selectedAlbum:
            html=album.bcid
    return html