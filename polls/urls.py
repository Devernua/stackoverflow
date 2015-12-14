# coding: utf-8
from django.contrib.auth.views import login, logout
from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
		url(r'^login/', login, {'template_name': 'polls/login.html'}, name='login'),

		url(r'^logout/', logout,{'template_name': 'polls/logout.html'}, name='logout'),
		# ex: /polls/
		url(r'^$', views.IndexView.as_view(), name='index'),
		# ex: /polls/5/
		url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
		# ex: /polls/5/results/
		url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),

		url(r'^tag/([\w-]+)/$', views.TagIndexView.as_view(), name='tag'),

		url(r'^hot/$', views.HotIndexView.as_view(), name='hot'),

		url(r'^(?P<question_id>[0-9]+)/answer/$', views.add_answer, name='answer'), 

		url(r'^ask/$', login_required(views.AskQuestion.as_view()), name='ask'),

		url(r'^ask/result/$', views.add_question, name='add_question'),

		url(r'^register/$', views.RegisterFormView.as_view(), name='register'),

		url(r'^register/result/$', views.add_user, name='add_user'),

		# ex: /polls/5/vote/
		#url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
		]
