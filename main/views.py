from django.shortcuts import render, get_object_or_404
from portfolio.models import Category, Product
from .forms import ContactForm


def index(request):
	content = {
		'products': Product.objects.all(),
	}
	return render(request, 'main/index.html', content)

def about(request):
	return render(request, 'main/about.html')

def portfolio(request):
	return render(request, 'main/portfolio.html')

def contact(request):
	error = ''
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
		else:
			error = 'Неверные данные!'


	content = {
		'form': ContactForm(),
		'error': error,
	}
	return render(request, 'main/contact.html', content)

def work(request, product_slug):
	product = get_object_or_404(Product, slug=product_slug)
	if product.id == 1:
		prev_product = get_object_or_404(Product, id=list(Product.objects.all())[-1].id)
	else:
		prev_product = get_object_or_404(Product, id=product.id - 1)
	if product.id == list(Product.objects.all())[-1].id:
		next_product = get_object_or_404(Product, id=1)
	else:
		next_product = get_object_or_404(Product, id=product.id + 1)
	content = {
		'product': product,
		'next_product': next_product,
		'prev_product': prev_product
	}
	return render(request, 'main/work.html', content)

