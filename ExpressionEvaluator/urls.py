from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from evaluator import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('evaluator/', include('evaluator.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
