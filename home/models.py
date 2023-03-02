from django.db import models

class ContactMessage(models.Model):
	title = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	detail = models.TextField(blank=True, null=True)
	reply = models.BooleanField(default=False)

	def __str__(self):
		return self.title