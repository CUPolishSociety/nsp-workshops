from django.forms import ModelForm
from django import forms

from workshops.models import WorkshopRegister

class WorkshopRegisterForm(ModelForm):
	class Meta:
		labels = {
			'uni':'University/Institution',
			'graduation':'Graduation year',
			'cv':'Upload your CV',
			'w_1':'1st preference',
			'w_2':'2nd preference',
			'w_3':'3rd preference',
		}

		help_texts={
			'email':'Please provide the email used at registration'
		}

		error_messages = {
			'email' : {
				'unique': 'You have already registered for workshops'
			}
		}


		model = WorkshopRegister  