from django.db import models


class TaskGroup(models.Model):
    name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Create your models here.
class ToDo(models.Model):
    taskgroup = models.ForeignKey(
        TaskGroup,
        related_name="tasks",
        related_query_name="task",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=100)
    Description = models.TextField()
    Date = models.DateField()
    Completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
