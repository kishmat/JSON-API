from django.db import models

# Create your models here.


class Member(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    real_name = models.CharField(max_length=100)
    tz = models.SlugField(max_length=100)


class Activity_period(models.Model):
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
