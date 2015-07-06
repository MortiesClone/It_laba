from __future__ import unicode_literals

from django.db import models

class Question(models.Model):
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	
class Choice(models.Model):
	poll = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)