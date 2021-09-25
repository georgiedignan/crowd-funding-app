from django.contrib.auth import get_user_model
from django.db import models
from datetime import date

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    not_for_profit = models.BooleanField(default=False)
    amount = models.IntegerField(null=True)
    image = models.URLField()
    is_open = models.BooleanField()
    location = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    # can create default
    date_created = models.DateField(default=date.today)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_projects'


    )

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
        )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='supporter_pledges'
        )
