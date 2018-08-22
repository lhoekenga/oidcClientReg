from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
#from tutorial.quickstart.serializers import UserSerializer, GroupSerializer
from api.serializers import UserSerializer, GroupSerializer, OIDCClientSerializer, GearClientSerializer
from api.models import OIDCClient, GearClient

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class OIDCClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows OIDC Clients to be viewed or edited.
    """
    queryset = OIDCClient.objects.all()
    serializer_class = OIDCClientSerializer


class GearClientViewSet(viewsets.ModelViewSet):
    queryset = GearClient.objects.all()
    serializer_class = GearClientSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the api index.")
