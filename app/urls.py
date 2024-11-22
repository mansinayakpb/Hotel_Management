from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import Home, SignUpView, UserLoginView

urlpatterns = [
    path("", Home.as_view(), name="home_page"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", UserLoginView.as_view(), name="login"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
