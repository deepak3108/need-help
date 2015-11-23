from django.db import models

# Create your models here.
class Database(models.Model):
	donar_name = models.CharField(max_length = 25)
	mobile_number = models.BigIntegerField()
	blood_group = models.CharField(max_length = 20)
	city_name = models.CharField(max_length = 20)	
