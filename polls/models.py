# coding: utf-8
import datetime

from django.conf 				import settings
from django.db 					import models
from django.utils 				import timezone
from django.contrib.auth.models import AbstractUser

#from taggit.managers import TaggableManager


class User(AbstractUser):
	avatar 	= models.ImageField(upload_to='avatars', blank=True, null=True)
	rating 	= models.IntegerField(default=0)


class Tag(models.Model):
	name 	= models.CharField(max_length = 40)

	def __str__(self):
		return self.name




class Question(models.Model):
	author 			= models.ForeignKey(settings.AUTH_USER_MODEL)
	question_title  = models.CharField(max_length = 200)
	question_text 	= models.CharField(max_length = 2000)
	pub_date 		= models.DateTimeField('date published')
	rating			= models.IntegerField(default=0)
	#tags_string 	= models.CharField(verbose_name=u'Tags', max_length=200, blank=True)
	#tags 			= models.ManyToManyField(Tag, null=True, blank=True)
	#tags 			= TaggableManager()
	tags 			= models.ManyToManyField(Tag)

	#def get_absolute_url(self):
	#	return reverse('polls/ask.html',)

	def __str__(self):
		return self.question_title

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)

	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'


class Answer(models.Model):
	author 		= models.ForeignKey(settings.AUTH_USER_MODEL)
	question 	= models.ForeignKey(Question)
	answer_text = models.CharField(max_length=2000)
	pub_date 	= models.DateTimeField('date published')
	rating 		= models.IntegerField(default = 0)
	is_correct 	= models.BooleanField(default = False)

	def __str__(self):
		return self.answer_text

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)

	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'


#class Choice(models.Model):
#	question 	= models.ForeignKey(Question)
#	choice_text = models.CharField(max_length=200)
#	votes		= models.IntegerField(default=0)

