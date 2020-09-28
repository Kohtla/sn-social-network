from django.urls import path
from .views import PostView

app_name = 'posts'


urlpatterns = [
    path('', PostView.as_view()),
]