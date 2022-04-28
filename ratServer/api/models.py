from django.db import models

# Create your models here.
class Command(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    instruction = models.CharField(max_length=200, blank=True, default='')
    treated = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']


class Response(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    command_instruction = models.CharField(max_length=200, blank=True, default='')
    value = models.TextField(blank = True, default='')

    class Meta:
        ordering = ['created']