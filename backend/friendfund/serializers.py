from rest_framework import serializers
from .models import Profile


class UserAccountSerializer(serializers.ModelSerializer):
    email = serializers.ReadOnlyField(source='user__email')
    balance = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ('email', 'mondo_user_id', 'balance')

    def get_balance(self, obj):
        return obj.balance(self.context['request'])
