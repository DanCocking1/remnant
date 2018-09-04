from django contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerilizer):
    class Meta:
        model = User
        fields = ('url', 'username','email', 'groups')


class GroupSerailizer(serializers.HyperlinkedModelSerilizer):
    class Meta:
        model = Group
        fields = ('url', 'name')
