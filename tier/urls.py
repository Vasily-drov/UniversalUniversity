from django.urls import path
from tier.views import FansList, FollowingList, CheckExpiration
# NewTier, CheckExpiration

urlpatterns = [
    #path('newtier/', NewTier, name='newtier'),
    path('fans_list/', FansList, name='fans_list'),
    path('following_list/', FollowingList, name='following_list'),
    #path('checkexp/', CheckExpiration, name='check-expiration'),
]