from django.conf.urls import url
from .views import UserAccountViewSet, ApiRootView, AuthenticationViewSet


urlpatterns = [
    url(r'^$', ApiRootView.as_view(), name='api-root'),
    url(r'^account/me$', UserAccountViewSet.as_view(), name='user-details'),
    url(r'^auth/login', AuthenticationViewSet.as_view(), name='auth-login'),
]
