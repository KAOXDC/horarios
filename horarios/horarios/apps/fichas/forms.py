from django import forms
from django.forms.extras import SelectDateWidget
from django.contrib.admin import widgets
from horarios.apps.fichas.models import Horario, Evento, Instructor, Aprendiz

class add_horario_form (forms.ModelForm):
	#fecha = forms.DateField(widget=forms.TextInput(attrs={'id':'datepicker'}))
	class Meta:
		model = Horario
		exclude = ('ficha','fecha',)

class add_evento_form (forms.ModelForm):
	class Meta:
		model = Evento
		exclude = ('horario',)

class add_instructor_form (forms.ModelForm):
	class Meta:
		model = Instructor
		
class add_aprendiz_form (forms.ModelForm):
	class Meta:
		model = Aprendiz
