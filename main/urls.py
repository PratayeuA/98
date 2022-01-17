from django.urls import path
from .views import index, about, portfolio, contact, work


urlpatterns = [
	path('', index, name='index'),
	path('about/', about, name='about'),
	path('portfolio/', portfolio, name='portfolio'),
	path('contact/', contact, name='contact'),
	path('work/<slug:product_slug>/', work, name='work'),
]