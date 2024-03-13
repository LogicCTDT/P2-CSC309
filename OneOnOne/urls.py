"""
URL configuration for OneonOne project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from rest_framework import routers
from Meeting.views import MeetingViewSet, UserViewSet, SuggestedMeetingView, MovingMeetingView
from Auth.views import LoginView, LogoutView, RegisterView, ProfileView, EditView


meetingrouter = routers.DefaultRouter()
meetingrouter.register(r'meetings', MeetingViewSet, basename='meeting')
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/<int:pk>/', include(meetingrouter.urls)),
    path('api/', include(router.urls)),
    path('api/<int:pk>/suggestedmeetings/', SuggestedMeetingView.as_view(), name='suggestedmeeting'),
    path('api/<int:pk>/movingsuggested/', MovingMeetingView.as_view(), name='movingsuggested'),
    path('api/token/', LoginView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/profile/', ProfileView.as_view(), name='profile'),
    path('api/edit/', EditView.as_view(), name='edit'),
]

urlpatterns += meetingrouter.urls

