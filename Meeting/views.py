from django.shortcuts import render

from Meeting.serializers import *
from rest_framework import viewsets, permissions, generics
from Meeting.models import *
# Create your views here.
class MeetingViewSet(viewsets.ModelViewSet):
    serializer_class = MeetingSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        userid = self.kwargs['pk']
        user = User.objects.get(id=userid)
        obj = Meeting.objects.filter(user1=user)
        return obj

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
