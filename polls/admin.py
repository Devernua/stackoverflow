# -*- coding: utf-8 -*-

from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Answer, Question, User, Tag 



class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
		(u'Дополнительно', 	{'fields': [ 'avatar']}),
		(None, 				{'fields': [ 'rating']}),
		)
    
	# def admin_avatar(self, instance):
	#     return instance.avatar and u'<img src="{0}" width="100px" />'.format(
	#         instance.avatar.url
	#     )
	# admin_avatar.allow_tags = True
	# admin_avatar.short_description = u'Аватар'

class AnswerInline(admin.StackedInline):
	model = Answer
	extra = 5


#class ChoiceInline(admin.StackedInline):
#   model = Choice
#   extra = 3

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		('Author',				{'fields': ['author']								}),
		(None,					{'fields': ['question_title']						}),
		(None,					{'fields': ['question_text']						}),
		('Date information',	{'fields': ['pub_date'], 'classes': ['collapse']	}),
		('Tags',				{'fields': ['tags']									}),
		('rating', 				{'fields': ['rating']								}),
	]

	inlines 		= [AnswerInline]#
	list_display 	= ('question_text', 'pub_date', 'was_published_recently')
	list_filter 	= ['pub_date']
	search_fields 	= ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Tag)
# Register your models here.
