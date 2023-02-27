from django.db import models

# Create your models here.

from django.urls import reverse
import uuid

class ElectoralProcess(models.Model):
    uuid = models.UUIDField(primary_key= True, default=uuid.uuid4, editable=False,auto_created= True)
    name = models.CharField(unique= True, max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    no_of_voters = models.IntegerField()
    unregistered_voters = models.IntegerField()
    link = models.SlugField(auto_created= True,unique=True)

    def get_absolute_url(self):
        return reverse('process_detail', args=[str(self.link)])

