# coding: utf-8
import datetime
from django import forms

from django.utils import timezone

from django.shortcuts 			import get_object_or_404, render
from django.http 				import HttpResponseRedirect
from django.core.urlresolvers 	import reverse
from django.views 				import generic

from .models 					import Question, Answer, User, Tag 

class AnswerForm(forms.Form):
	text = forms.CharField(widget = forms.Textarea(attrs={'rows':'8', 'class':'form-control', 'placeholder': 'Enter your answer here'}))

class QuestionForm(forms.Form):
	title = forms.CharField(max_length = 200, widget=forms.TextInput(attrs={'class' : 'form-control'}))
	text  = forms.CharField(widget = forms.Textarea(attrs={'rows':'8', 'class':'form-control', 'placeholder': 'Enter your question here'}))
	tags  = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={'class' : 'form-control'}))



class RegistrationForm(forms.Form):
	username 	= forms.CharField(max_length = 200, widget=forms.TextInput(attrs={'class' : 'form-control'}))
	password1 	= forms.CharField(label=u'password', widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
	password2 	= forms.CharField(label=u'again', widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
	email 		= forms.EmailField(max_length = 200, widget=forms.TextInput(attrs={'class' : 'form-control'}))
	avatar 		= forms.ImageField(required=False)

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			User.objects.get(username = username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError(('duplicate_username'), code='duplicate_username')

	def clean(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if (password1 == password2):
			return self.cleaned_data
		else:
			raise forms.ValidationError(('enter password again'), code='invalid_password')

#			raise render(request, 'polls/register.html', {
#		'error_message': "enter password again",
#		'form':self,
#		})

#class Meta(UserCreationForm.Meta):
#	model = User
#	def clean_username(self):
#		username = self.cleaned_data['username']
#
#		try:
#			self.Meta.model.objects.get(username = username)
#		except self.Meta.model.DoesNotExist:
#			return username
#		raise forms.ValidationError(
#			self.error_messages['duplicate_username'],
#			code='duplicate_username',
#		)




