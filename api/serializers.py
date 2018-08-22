from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import OIDCClient, GearClient


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class OIDCClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OIDCClient
        #fields = ('url', 'client_id', 'client_secret', 'redirect_url')
        fields = ('url', 'client_id', 'client_secret', 'client_name', 'contact_email', 'redirect_url')
        #fields = ('__all__')


class GearClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = GearClient
        fields = ('client_id', 'client_secret', 'redirect_url')
