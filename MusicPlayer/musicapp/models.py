from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='songs')
    path = models.CharField(max_length=255)

    def __str__(self):
        return self.title
