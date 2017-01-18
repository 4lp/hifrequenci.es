from django.db import models

class BCAlbum(models.Model):
    name = models.CharField(max_length=1000)
    bcid = models.CharField(max_length=10000, default="")
    selectedAlbum = models.BooleanField("Selected Album?", default=False)

    def save(self, *args, **kwargs):
        if self.selectedAlbum:
            try:
                temp = BCAlbum.objects.get(selectedAlbum=True)
                if self != temp:
                    temp.selectedAlbum = False
                    temp.save()
            except BCAlbum.DoesNotExist:
                pass
        super(BCAlbum, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
