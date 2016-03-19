from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^store/', include('store.urls'), name='store'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),
    ]
