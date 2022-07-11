from django.urls import URLPattern, path
from . import views


urlpatterns = [
    path('posts/', views.PostList.as_view()),
]