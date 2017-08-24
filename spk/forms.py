from django import forms

from .models import MailMe

class MailMeForm(forms.ModelForm):
	class Meta:
		model = MailMe
		fields = [
			'email',
			'fullName',
			'message',
		]
