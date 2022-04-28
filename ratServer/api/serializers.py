from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Command, Response


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class CommandSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    instruction = serializers.CharField(required=False, allow_blank=True, max_length=200)
    treated = serializers.BooleanField(required=False)

    class Meta:
        model = Command
        fields = ['created', 'id', 'instruction', 'treated']

class ResponseSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Response
        fields = ['id', 'created', 'command_instruction', 'value']
