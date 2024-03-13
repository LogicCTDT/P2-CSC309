

from rest_framework import routers, serializers, viewsets
from Meeting.models import *

class MeetingSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="meeting-detail")
    class Meta:
        model = Meeting
        fields = ['url', 'id', 'user1', 'user2', 'start_time', 'duration']

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password', 'is_superuser')

class SuggestedChildSerializer(serializers.Serializer):
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()
    preference1 = serializers.BooleanField()
    preference2 = serializers.BooleanField()
    user = serializers.CharField()
    def to_representation(self, instance):
        response_dict = dict()
    
        response_dict['start_time'] = instance[0]
        response_dict['end_time'] = instance[1]
        response_dict['preference1'] = instance[2]
        response_dict['preference2'] = instance[3]
        response_dict['user'] = instance[4]
        
        return super(SuggestedChildSerializer, self).to_representation(response_dict)
    
    
    
class SuggestedMeetingSerializer(serializers.Serializer):
    user = serializers.CharField()
    meetings = serializers.ListField(child=SuggestedChildSerializer())

    def __init__(self, *args, **kwargs):
        self.user = kwargs['context']['user'].username
        super(SuggestedMeetingSerializer, self).__init__(*args, **kwargs)
    def to_representation(self, instance):
        response_dict = dict()
        response_dict['user'] = self.user
        
        response_dict['meetings'] = instance
       
        return super(SuggestedMeetingSerializer, self).to_representation(response_dict)
    
class MovingSuggestedSerializer(serializers.Serializer):
    first = SuggestedChildSerializer()
    second = SuggestedChildSerializer()
    def to_representation(self, instance):
        
        response_dict = dict()
    
        response_dict['start_time'] = instance[0]
        response_dict['end_time'] = instance[1]
        response_dict['preference'] = instance[2]
        response_dict['user'] = instance[3]
        
        return super(MovingSuggestedSerializer, self).to_representation(response_dict)