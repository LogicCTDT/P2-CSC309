

from rest_framework import routers, serializers, viewsets
from Meeting.models import *

class MeetingSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="meeting-detail")
    class Meta:
        model = Meeting
        fields = ['url', 'id', 'user1', 'user2', 'start_time', 'duration']

class CalendarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Calendar
        fields = ['id', 'user']
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password', 'is_superuser')