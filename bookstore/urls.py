from django.conf.urls import include, url
from django.contrib import admin
from registration.backends.simple.views import RegistrationView

# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/store/'

urlpatterns = [
	url(r'^store/', include('store.urls'), name='store'),
    #This pattern alone takes users to a registrationc complete page
    #url(r'^accounts/', include('registration.backends.default.urls')),
    #This url pattern returns user to main index page after registration. 
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', include(admin.site.urls)),
    ]
