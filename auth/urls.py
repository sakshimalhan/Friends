from django.urls import path
from auth import views
urlpatterns=[
    path('login',views.Login.as_view()),
    path('logout',views.logout.as_view()),
    path('signup',views.signup.as_view())
]