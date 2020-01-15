from django.db import models

# Create your models here.
class Article_Class(models.Model):
	title = models.CharField(max_length = 120)
	content = models.TextField()
	age = models.TextField()


	def __str__ (self):
		return self.title + " " + str(self.age)
	
		