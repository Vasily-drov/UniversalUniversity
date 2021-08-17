from django.urls import path
from post.views import NewPost, PostDetails, like, bookmark, BookmarkList ,Statistic

urlpatterns = [
    path('newpost/', NewPost, name='newpost'),
    path('statistic/', Statistic, name='statistic'),
    path('<uuid:post_id>',PostDetails, name='postdetails'),
    path('<uuid:post_id>/like',like, name='postlike'),
    path('<uuid:post_id>/bookmark',bookmark, name='postbookmark'),
]