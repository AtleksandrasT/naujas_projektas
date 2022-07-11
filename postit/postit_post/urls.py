from django.urls import URLPattern, path
from . import views


urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('posts/<int:pk>/comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/comments/', views.CommentList.as_view()),
]