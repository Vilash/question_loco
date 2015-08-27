from django.db import models

# Create your models here.

class Question(models.Model):
	created_at	=	models.DateTimeField(auto_now_add=True)
	question	=	models.TextField()
	order		=	models.IntegerField(default=0)
	category	=	models.CharField(max_length=255)
	class Meta(object):
		ordering	= 	['order']
			

	def __str__(self):
		return self.question