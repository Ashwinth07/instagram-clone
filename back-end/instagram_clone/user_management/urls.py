from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UsersAPI, UserAPI

urlpatterns = [
    # path('comments/', CommentAPI.as_view()),
    path('User/', UsersAPI.as_view()),
    path('user/', UserAPI.as_view()),
]