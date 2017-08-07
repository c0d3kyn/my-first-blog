# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Post(models.Model):
# class define un objeto / Post es nuestro modelo / models.Models indica que post es un modelo de Django (lo guarda en la BD)
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
		default = timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
