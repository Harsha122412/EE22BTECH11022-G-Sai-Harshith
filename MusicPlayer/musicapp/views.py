from django.shortcuts import render
from django.conf import settings
import os

def index(request):
    songs_dir = os.path.join(settings.BASE_DIR, 'musicapp/static/songs')
    songs = []
    for filename in os.listdir(songs_dir):
        if filename.endswith('.mp3'):
            title = os.path.splitext(filename)[0]
            path = f'/static/songs/{filename}'
            songs.append({'title': title, 'path': path})
    return render(request, 'musicapp/index.html', {'songs': songs})
