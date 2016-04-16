from collections import OrderedDict
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import login, logout, authenticate
from rest_framework.generics import RetrieveAPIView
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework import views
from mondo.exceptions import MondoApiException
from .serializers import UserAccountSerializer
from .models import Profile
from .utils import generate_mondo_auth_url, generate_state_token, exchange_authorization_code_for_access_token


class ApiRootView(views.APIView):
    """
    List of all enpoints available with this API
    """
    _ignore_model_permissions = True

    def get(self, request, *_args, **_kwargs):
        ret = OrderedDict([
            ('auth', reverse('auth-login', request=request)),
            ('my-account', reverse('user-details', request=request)),
        ])
        return Response(ret)


class UserAccountView(views.APIView):

    def get(self, request, *_args, **_kwargs):
        data = Profile.objects.get(pk=1)
        serializer = UserAccountSerializer(data, context={'request': request})
        return Response(serializer.data)


class AuthenticationViewSet(views.APIView):

    def get(self, request, *_args, **_kwargs):
        if request.user.is_authenticated():
            raise PermissionDenied('You must be signed out')
        code, state = request.GET.get('code', None), request.GET.get('state', None)
        callback = reverse('auth-login', request=request)
        if code:
            try:
                if 'oauth_state' not in request.session or request.session['oauth_state'] != state:
                    raise PermissionDenied('Invalid OAuth state')
                access_token, refresh_token, user_id = exchange_authorization_code_for_access_token(
                    settings.MONDO_CLIENT_ID, settings.MONDO_CLIENT_SECRET, code, callback)

                profile, _ = Profile.objects.get_or_create(mondo_user_id=user_id)
                profile.refresh_token = refresh_token
                profile.save()

                user = authenticate(username=profile.user.username)
                login(request, user)
                request.session['access_token'] = access_token
                profile.populate_account(request)
                return Response({'status': 'ok'})

            except MondoApiException:
                raise PermissionDenied('Invalid OAuth authentication')
        else:
            state = generate_state_token()
            request.session['oauth_state'] = state
            url = generate_mondo_auth_url(settings.MONDO_CLIENT_ID, callback, state)
            return HttpResponseRedirect(url)

    def delete(self, request, *_args, **_kwargs):
        if not request.user.is_authenticated():
            raise PermissionDenied('You must be signed in')
        request.session['access_token'] = None
        logout(request)
