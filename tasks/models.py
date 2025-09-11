from django.db import models
from django.utils import timezone


class Status(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    deadline = models.DateTimeField()

    def __str__(self):
        return self.title

class SubTask(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    deadline = models.DateTimeField()
    task = models.ForeignKey(Task, related_name='subtasks', on_delete=models.CASCADE) # Связь с основной задачей

    def __str__(self):
        return self.title

