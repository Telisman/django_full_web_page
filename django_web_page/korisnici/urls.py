from django.urls import path
from django.urls import re_path,include
from django.conf import settings
from . import views
from django.conf.urls import url
from .views import LikeView,PostPerCategory,PostHomeView,PostDetail,NavFooter,PostPageView,AddPost,UpdatePost,DeletePostView,ShowProfile,MajstoriView,MajstoriProfile,AddComment,MyPosts,MyPosts2
from django.views.static import serve 


urlpatterns = [
    path('navbar', NavFooter, name='Nav_Footer'),
	path('post-category/<int:pk>', PostPerCategory, name='post-category'),
    path('', PostHomeView.as_view(), name ='home'),
    path('PostDetail/<int:pk>', PostDetail.as_view(), name ='post_detail'),
    path('PostPage/', PostPageView, name ='post_page'),
    path('MyPosts/', MyPosts, name ='my-posts'),
    path('MyPosts2/', MyPosts2, name ='my-posts2'),
    path('AddPost/<int:pk>/', AddPost.as_view(), name = 'add_post'),
    path('PostDetail/UpdatePost/<int:pk>', UpdatePost.as_view(), name = 'update'),
    path('DeletePost/<int:pk>/', DeletePostView.as_view(), name = 'delete'),
    path('Profile/<int:pk>/', ShowProfile.as_view(), name = 'profile'),
    path('like/<int:pk>', LikeView, name="like_post"),
    path('Majstori/',MajstoriView.as_view(), name="majstori_view"),
    path('ProfileMajstori/<int:pk>',MajstoriProfile.as_view(), name="majstori_profile"),
    path('PostDetail/<int:pk>/Add_comment', AddComment.as_view(), name="add_comment"),
    url(r'^messages/', include('django_messages.urls')),	
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
