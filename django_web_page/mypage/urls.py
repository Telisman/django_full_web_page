
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('korisnici.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    url(r'^messages/', include('django_messages.urls')),
	

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
