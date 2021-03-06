from django.db import models

from django.contrib.auth.models import User

class Organization(models.Model):
    name = models.CharField(max_length=40)
    website = models.URLField()
    email = models.EmailField()
    freicoin_address = models.CharField(max_length=34)
    bitcoin_address = models.CharField(max_length=34, blank=True)
    short_description = models.CharField(max_length=350)
    long_description = models.CharField(max_length=1500)
    foundation_address = models.CharField(max_length=34, blank=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name
