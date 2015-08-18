import datetime
from django.db import models

def file_name(instance,filename):
		new_filename = instance.name.lower().replace(' ', '_')+'_'+instance.surname.lower().replace(' ', '_') +'.pdf'

		return 'cv/'+new_filename

class WorkshopRegister(models.Model):
	name = models.CharField(max_length=250)
	surname = models.CharField(max_length=250)
	email = models.EmailField(max_length=75, unique=True)
	uni = models.CharField(max_length=200)
	graduation = models.IntegerField(choices=[(x,x) for x in range (1980, 2021)])

	WORKSHOP_CHOICES = (
			('bain','Bain&Company'),
			('bzwbk','Bank Zachodni WBK'),
			('pwc','PwC'),
			('uber','Uber'),
			('martap', 'Marta Poslad'),
		)

	

	w_1 = models.CharField(max_length=30, choices=WORKSHOP_CHOICES)
	w_2 = models.CharField(max_length=30, choices=WORKSHOP_CHOICES)
	w_3 = models.CharField(max_length=30, choices=WORKSHOP_CHOICES, blank = True)
	cv = models.FileField(upload_to=file_name, blank=True)
