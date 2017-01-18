from django.db import models

class Entry(models.Model):
    name = models.CharField(max_length=1000)
    date = models.DateTimeField()
    content = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['date']

