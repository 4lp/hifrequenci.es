from django.http import HttpResponse, Http404
import random
import json
import soundcloud

buttonCode = """
            <div class="btn btn-primary btn-mini" type="submit" href="#" id="soundcloud-button">
            load random song</div>
            """
CLIENT_ID = "c7edd2599a1c8e491d123056a75a61c3"
USER_ID = "1221567"

client = soundcloud.Client(client_id=CLIENT_ID)

def makePlayer(request):
    html = ""
    tracks = client.get('/users/%s/tracks' % USER_ID)
    uri = tracks[0].uri
    html = """<iframe align="middle" style="width:100%%;height:150px;border:none;margin:20;padding:0;"
                src="https://w.soundcloud.com/player/?visual=true&url=%s&show_artwork=true
                &client_id=c7edd2599a1c8e491d123056a75a61c3"></iframe>
                %s""" % (uri, buttonCode)
    return html

def buttonClicked(request):
    if request.is_ajax():
        tracks = client.get('/users/%s/tracks' % USER_ID)
        length = len(tracks)
        rand = random.randint(0, length)
        uri = tracks[rand].uri
        html = """<iframe align="middle" style="width:100%%;height:150px;border:none;margin:20;padding:0;"
                src="https://w.soundcloud.com/player/?visual=true&url=%s&show_artwork=true&auto_play=true
                &client_id=c7edd2599a1c8e491d123056a75a61c3"></iframe>
                %s""" % (uri, buttonCode)
        data = json.dumps(html)
        return HttpResponse(data, content_type='application/json')
    else:
        raise Http404