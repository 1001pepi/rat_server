from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import UserSerializer, GroupSerializer, CommandSerializer, ResponseSerializer
from api.models import Command, Response


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


class CommandViewSet(viewsets.ModelViewSet):

    queryset = Command.objects.all()
    serializer_class = CommandSerializer


class ResponseViewSet(viewsets.ModelViewSet):

    queryset = Response.objects.all()
    serializer_class = ResponseSerializer