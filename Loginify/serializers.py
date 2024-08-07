from rest_framework import serializers
from LoginSystem.Loginify.models import UserDetails

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ['username', 'email', 'password']
