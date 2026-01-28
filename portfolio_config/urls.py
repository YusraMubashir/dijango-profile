from django.contrib import admin
from django.urls import path
from bio.views import portfolio_home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', portfolio_home, name='home'),
]

# Add this to handle images during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)