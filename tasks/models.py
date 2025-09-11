from django.db import models
from django.utils import timezone
from django.utils.html import format_html

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
        return self.title  # Полное название для выбора в формах

    def short_title(self):
        """Возвращает укороченное название с ... если длиннее 10 символов"""
        if len(self.title) > 10:
            return f"{self.title[:10]}..."
        return self.title
    short_title.short_description = "Title"

class SubTask(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    deadline = models.DateTimeField()
    task = models.ForeignKey(Task, related_name='subtasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.title  # Полное название для выбора в формах

    def short_title(self):
        """Возвращает укороченное название с ... если длиннее 10 символов"""
        if len(self.title) > 10:
            return f"{self.title[:10]}..."
        return self.title
    short_title.short_description = "Title"