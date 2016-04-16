from rest_framework import serializers
from .models import Profile


class UserEmailField(serializers.EmailField):

    def to_representation(self, obj):
        return obj.user.email if hasattr(obj, 'user') else None

    def to_internal_value(self, data):
        user = self.parent.instance.user
        user.email = data
        user.save()
        return {
            "user": user,
        }


class UserAccountSerializer(serializers.ModelSerializer):
    email = UserEmailField(source='*')
    mondo_balance = serializers.SerializerMethodField()
    suggested_lend = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ('email', 'mondo_user_id', 'mondo_balance')
        read_only_fields = ('mondo_user_id',)

    def get_mondo_balance(self, obj):
        return obj.balance(self.context['request'])

    def suggested_lend(self, obj):
        return obj.balance(self.context['request'])
