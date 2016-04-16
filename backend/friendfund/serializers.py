from rest_framework import serializers
from .models import Profile


class UserAccountSerializer(serializers.ModelSerializer):
    email = serializers.ReadOnlyField(source='user__email')

    class Meta:
        model = Profile
        fields = ('email', 'mondo_user_id', 'balance')
