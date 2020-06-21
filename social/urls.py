from django.urls import path
from social import views
urlpatterns=[
    path('home/',views.Home.as_view()),
    path('post/',views.post.as_view()),
    path('myfriends/',views.myfriends.as_view()),
    path('post/<int:pk>/like',views.PostLike.as_view()),
    path('',views.wall.as_view())
]