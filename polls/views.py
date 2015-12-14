# coding: utf-8
import datetime
from django.utils 				import timezone
from django.views.generic.edit 	import FormView
from django.shortcuts 			import get_object_or_404, render
from django.http 				import HttpResponseRedirect
from django.core.urlresolvers 	import reverse
from django.views 				import generic
from django.core.mail 			import send_mail

from django.core.files.uploadedfile import SimpleUploadedFile

from .models 					import Question, Answer, User, Tag 
from .							import forms
#from django import forms
#from django.forms import ModelForm, Textarea

#from taggit.models import Tag
#from taggit.managers import TaggableManager


#class AnswerForm(django.forms.Form):
#	title = django.forms.CharField(max_length=200) 
#    class Meta: 
#        model = Answer
#        fields = 'answer_text' 

def popular_tags():
	return Tag.objects.all()[:20]


class IndexView(generic.ListView):
	template_name       = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""Return the last five published questions."""
		return Question.objects.order_by('-pub_date')[:20]

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['tags'] = popular_tags()
		return context

class HotIndexView(generic.ListView):
	template_name       = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""Return the last five published questions."""
		return Question.objects.order_by('-rating')[:20]
	

	def get_context_data(self, **kwargs):
		context = super(HotIndexView, self).get_context_data(**kwargs)
		context['tags'] = popular_tags()
		return context


class TagIndexView(generic.ListView):
	template_name       = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		self.tags = get_object_or_404(Tag, name=self.args[0])
		"""Return the last five published questions."""
		return Question.objects.filter(tags=self.tags)[:20]

	def get_context_data(self, **kwargs):
		context = super(TagIndexView, self).get_context_data(**kwargs)
		context['tags'] = popular_tags()
		return context

#def tag (request, tag_id): # тут все тоже самое
#	tag 		= Tag.objects.select_related().get(id=id)
#	questions 	= tag.question_set.all()
#	count 		= tag.question_set.count();
#	return render(request, 'tagpage.html', {'questions': questions, 'tag': tag})


class DetailView(generic.DetailView):
	model 			= Question
	template_name 	= 'polls/detail.html'

	def popular_tags(self):
		return Tag.objects.all()[:20]

	def get_context_data(self, **kwargs):
		context = super(DetailView, self).get_context_data(**kwargs)
		context['tags'] = popular_tags()
		context['form'] = forms.AnswerForm()
		return context



class ResultsView(generic.DetailView):
	model 			= Question
	template_name 	= 'polls/results.html'

class AskQuestion(FormView):
	template_name = 'polls/ask.html'
	form_class = forms.QuestionForm
	success_url = '/polls/ask/result/'

class RegisterFormView(FormView):
	form_class = forms.RegistrationForm
	success_url = "polls/login/"
	template_name = "polls/register.html"
	#def form_valid(self, form):
	#	form.save()
	#	return super(ResultsView, self).form_valid(form)


def add_user(request):
	if request.method == 'POST':
		form = forms.RegistrationForm(request.POST, request.FILES)
		if form.is_valid():
			cd = form.cleaned_data
			u = User.objects.create_user(
				username 	= cd['username'],
				email 		= cd['email'],
				password 	= cd['password1'],
				avatar		= cd['avatar'],
				)

			
			u.save()
			return HttpResponseRedirect(reverse('polls:login') )
	return render(request, 'polls/register.html', {
		'error_message': "Sorry",
		'form':form,
		})

def add_question(request):
	form = forms.QuestionForm(request.POST or None)
	if request.method == "POST" and form.is_valid():
		question = Question(question_title = form.cleaned_data['title'], question_text = form.cleaned_data['text'])
		question.author = request.user
		question.pub_date = timezone.now()
		question.save()
		#if (request.user.email != ''):
		#	send_mail(question.author, question.question_text, 'devernua@mail.ru', [request.user.email])
		return HttpResponseRedirect(reverse('polls:index') )
	return render(request, 'polls/ask.html', {
		'error_message': "You didn't enter question.",
		'form':form,
		})


def add_answer(request, question_id):
	p = get_object_or_404(Question, pk = question_id)
	form = forms.AnswerForm(request.POST or None)
	if request.method == "POST" and form.is_valid():
		answ = Answer(question = p, answer_text = form.cleaned_data['text'])
		answ.author = request.user
		answ.pub_date = timezone.now()
		answ.save()
		return HttpResponseRedirect(reverse('polls:detail', args=(p.id,)))
	return render(request, 'polls/detail.html', {
		'question':p,
		'error_message': "You didn't enter answer.",
		'form':form,
		})






	#try:
		
	#	answ = p.answer_set.create(author=request.user, question = p, answer_text = tmp, pub_date = timezone.now())
	#except (KeyError, Answer.DoesNotExist):
	#	return render(request, 'polls/detail.html', {
	#		'question': p,
	#		'error_message': tmp,
	#	})
	#
	#else:
	#
	#	answ.save()
	#	return HttpResponseRedirect(reverse('polls:detail', args=(p.id,)))


#def vote(request, question_id):
#	p = get_object_or_404(Question, pk=question_id)
#    	try:
#        	selected_choice = p.choice_set.get(pk=request.POST['choice'])
#    	except (KeyError, Choice.DoesNotExist):
#        	# Redisplay the question voting form.
#        	return render(request, 'polls/detail.html', {
#            		'question': p,
#            		'error_message': "You didn't select a choice.",
#        	})
#    	else:
#        	selected_choice.votes += 1
#        	selected_choice.save()
#       	 	# Always return an HttpResponseRedirect after successfully dealing
#       	 	# with POST data. This prevents data from being posted twice if a
#        	# user hits the Back button.
#        	return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
