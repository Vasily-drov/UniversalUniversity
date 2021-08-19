from django.urls import path
from tier.views import FansList, FollowingList
# NewTier, CheckExpiration

urlpatterns = [
    #path('newtier/', NewTier, name='newtier'),
    path('myfans/', FansList, name='myfans'),
    path('myfollowers/', FollowingList, name='myfollowers'),
    #path('checkexp/', CheckExpiration, name='check-expiration'),
]