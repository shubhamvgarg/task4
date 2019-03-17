from django.db import models


class Images(models.Model):
	name = models.CharField(max_length=200,unique=True)
	description = models.TextField(null=True)
	createdby=models.TextField(null=True)
	image = models.FileField(upload_to='pictures/%Y/%m/%d/', max_length=255, null=True, blank=True)
	def __str__(self):
		return self.name