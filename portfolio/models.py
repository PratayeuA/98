from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):

	name = models.CharField('Категория', max_length=20, unique=True)
	slug = models.SlugField('URL', unique=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'
		ordering = ('name', )

class Product(models.Model):

	title = models.CharField('Заголовок', max_length=50, unique=True)
	description = models.TextField('Описание')
	image = models.ImageField('Картинка', upload_to='static/portfolio')
	slug = models.SlugField('URL', unique=True)
	cat = models.ManyToManyField(Category, verbose_name='Категории')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('work', kwargs={'product_slug': self.slug})

	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'
		ordering = ('title', )
