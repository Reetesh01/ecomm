from django.db import models

# Create your models here.
# category
# suncategory
# ads
# slider
# products
# brand

class Category(models.Model):
	name = models.CharField(max_length = 300)
	slug = models.TextField()

	def __str__(self):
		return self.name

class SubCategory(models.Model):
	name = models.CharField(max_length = 300)
	category = models.ForeignKey(Category,on_delete = models.CASCADE, default = 1)
	slug = models.TextField()

	def __str__(self):
		return self.name

class Ad(models.Model):
	name = models.CharField(max_length = 500)
	image = models.ImageField(upload_to = 'media')
	link = models.URLField(max_length = 500 , blank = True)
	rank = models.IntegerField() 

	def __str__(self):
		return self.name

class Slider(models.Model):
	name = models.CharField(max_length = 400)
	image = models.ImageField(upload_to = 'media')
	rank = models.IntegerField()
	status = models.CharField(max_length = 500, choices = (('active','Active'),('', 'Default')))

	def __str__(self):
		return self.name