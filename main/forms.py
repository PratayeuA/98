from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = '__all__'
		# <input type="text" class="form-control" placeholder="Name">
		# <input type="text" class="form-control" placeholder="Email">
		# <textarea name="" id="message" cols="30" rows="7" class="form-control" placeholder="Message"></textarea>
		widgets = {
			'name': forms.TextInput(
					attrs={
						'class': 'form-control',
						'placeholder': 'Имя',
					}
				),
			'email': forms.TextInput(
					attrs={
						'class': 'form-control',
						'placeholder': 'Почта',
					}
				),
			'message': forms.Textarea(
					attrs={
						'id': 'message',
						'cols': '30',
						'rows': '7',
						'class': 'form-control',
						'placeholder': 'Сообщение',
					}
				)
		}

