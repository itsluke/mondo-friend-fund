from rest_framework.generics import RetrieveAPIView
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import views
from collections import OrderedDict
from .serializers import UserAccountSerializer
from .models import Profile


class ApiRootView(views.APIView):
    """
    List of all enpoints available with this API
    """
    _ignore_model_permissions = True

    def get(self, request, *_args, **_kwargs):
        ret = OrderedDict([
            ('my-account', reverse('user-details', request=request)),
        ])
        return Response(ret)


class UserAccountView(views.APIView):

    def get(self, request, *_args, **_kwargs):
        data = Profile.objects.get(pk=1)
        serializer = UserAccountSerializer(data)
        return Response(serializer.data)
