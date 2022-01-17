from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):
	# phonenumber = PhoneNumberField(verbose_name='Телефон', unique=True)
	name = models.CharField('Имя', max_length=20)
	email = models.EmailField('Почта', unique=True)
	message = models.TextField('Сообщение')

	def __str__(self):
		return self.email

	class Meta:
		verbose_name = 'Контакт'
		verbose_name_plural = 'Контакты'
		ordering = ('name', 'email', )