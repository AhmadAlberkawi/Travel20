from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('TravelBook.urls')),
    path('account/',include('account.urls')),
    path('weather/',include('Weth_Ne.urls')),


]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)