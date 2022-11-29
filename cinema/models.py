from django.db import models


class Cinema(models.Model):
	name = models.CharField(max_length=50)
	location = models.TextField(max_length=50)
	contacts = models.TextField(max_length=20)
