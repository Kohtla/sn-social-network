from rest_framework import serializers

from users.models import User


class UserSmallSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('last_login', 'last_action')
