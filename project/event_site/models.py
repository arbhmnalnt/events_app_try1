from django.db import models
from django.utils import timezone
from django.conf import settings
from django.db import models
from django.urls import reverse


class Event(models.Model):
    STATUS_CHOICES = (('Published', 'published'), ('Draft', 'draft'))
    title            = models.CharField(max_length=250)
    slug             = models.SlugField(max_length=250, unique_for_date='date') 
    creator          = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='events_u')
    description      = models.TextField()
    date             = models.DateTimeField(default=timezone.now) 
    created          = models.DateTimeField(auto_now_add=True)
    updated          = models.DateTimeField(auto_now=True)
    status           = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')
    participants_num = models.IntegerField(default=0)


    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.title

    def get_username(self):
        if self.creator:
            email = str(self.creator)
            return email.split("@")[0]
        else:
            None
    
    def get_absolute_url(self):
        #pylint: disable=E1101
        return reverse('events:event_detail',args=[self.date.year,self.date.month,self.date.day, self.slug])

class Eventparticipant(models.Model):
    user_id  = models.IntegerField() 
    event_id = models.IntegerField()

