from django.db import models

class Todo(models.Model):
    class Status(models.TextChoices):
        COMPLETED = 'CP'
        IN_PROGRESS = 'IP'
        NOT_STARTED = 'NS'
        FAILED = 'FA'
        
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    status = models.CharField(max_length=2,choices = Status.choices)
    