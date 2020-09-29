from django.urls import path
from .views import LikesAnalyticsView, UserAnalyticsView

app_name = 'analytics'


urlpatterns = [
    path('', LikesAnalyticsView.as_view()),
    path('/user', UserAnalyticsView.as_view())
]