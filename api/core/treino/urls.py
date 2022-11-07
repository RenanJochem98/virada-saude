from django.urls import path, include

from treino.api import urls

urlpatterns = [
    path("api/", include(urls)),
]
