from django.conf.urls import url
from .views import UserAccountView, ApiRootView, AuthenticationViewSet


urlpatterns = [
    url(r'^$', ApiRootView.as_view(), name='api-root'),
    url(r'^account/me$', UserAccountView.as_view(), name='user-details'),
    url(r'^auth/login', AuthenticationViewSet.as_view(), name='auth-login'),
]
