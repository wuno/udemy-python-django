from django.shortcuts import render
from . models import Book
# Create your views here.
def index(request):
	return render(request, 'template.html')

def store(request):
	count = Book.objects.all().count()
	context = {
		'count': count,
		'page': 'Welcome to my super cool app!',
	}
	request.session['location'] = "unknown"
	if request.user.is_authenticated():
		request.session['location'] = "Earth"
	return render(request, 'base.html', context)
