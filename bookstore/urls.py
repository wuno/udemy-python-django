from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^store/', include('store.urls'), name='store'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
    #url('', include('django.contrib.auth.urls', namespace='auth')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 


   	  