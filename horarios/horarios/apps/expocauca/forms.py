from django import forms
from django.forms.extras import SelectDateWidget
from django.contrib.admin import widgets
from horarios.apps.expocauca.models import *

class add_persona_form (forms.ModelForm):
	#fecha = forms.DateField(widget=forms.TextInput(attrs={'id':'datepicker'}))
	class Meta:
		model = Persona
		exclude = ('fecha_registro',)

class add_programa_form (forms.ModelForm):
	class Meta:
		model = Programa

