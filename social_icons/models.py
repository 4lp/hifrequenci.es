from django.db import models

class NetworkChoices(models.Model):
    name = models.CharField(max_length=1000, editable=False)
    glyphname = models.CharField(max_length=1000, editable=False)

    def __str__(self):
        return self.name

class SocialIcon(models.Model):
    name = models.CharField(max_length=1000)
    url = models.CharField("Social media page url", max_length=10000)
    isSelected = models.BooleanField("Show this icon?", default=False)
    selectedNetworks = models.ManyToManyField(NetworkChoices)

    def __str__(self):
        return self.name





