from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Event(models.Model):
    STATUS_CHOICES = (('Draft', 'draft'), ('Published', 'publish'))
    title        = models.CharField(max_length=250)
    slug         = models.SlugField(max_length=250, unique_for_date='publish') 
    creator      = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events_u')
    description  = models.TextField()
    date         = models.DateTimeField(default=timezone.now) 
    created      = models.DateTimeField(auto_now_add=True)
    updated      = models.DateTimeField(auto_now=True)
    status       = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.title

class Eventparticipant(models.Model):
    user_id  = models.IntegerField() 
    event_id = models.IntegerField()