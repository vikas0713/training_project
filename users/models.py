from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Profile(AbstractUser):
	"""
	Custom user model
	"""
	display_picture = models.FileField(upload_to='uploads/', blank=True, null=True)

	def __str__(self):
		return self.username