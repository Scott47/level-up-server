from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import usergame_list

urlpatterns = [
    path('reports/usergames', usergame_list),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)