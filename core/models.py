from django.db import models


class Core(models.Model):
	"""
	Basic information about any model
	"""
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	slug = models.SlugField(unique=True)

	class Meta:
		abstract = True
