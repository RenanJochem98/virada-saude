from django.urls import path, include

from empresa.api import urls
# from users.views import register_cpf

urlpatterns = [
    path("api/", include(urls)),
    # path("register/<str:string>", register_cpf, name="register"),
]
