from django.urls import path
from .views import PostView, LikeView

app_name = 'posts'


urlpatterns = [
    path('', PostView.as_view()),
    path('/like/<int:post>', LikeView.as_view())
]