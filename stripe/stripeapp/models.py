from django.db import models

# Create your models here.
class Plan(models.Model):
    plan_name=models.TextField()
    monthly_price=models.IntegerField()
    yearly_price=models.IntegerField()
    video_quality=models.TextField()
    resolution=models.TextField()
    ph=models.IntegerField()
    tab=models.IntegerField()
    comp=models.IntegerField()
    tv=models.IntegerField()
    no_active=models.IntegerField()