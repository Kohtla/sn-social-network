from django.urls import path
from users.views import UserView
from rest_framework_simplejwt import views as jwt_views

app_name = 'users'

urlpatterns = [
    path('', UserView.as_view()),
    path('/token', jwt_views.TokenObtainPairView.as_view()),
    path('/token/refresh', jwt_views.TokenRefreshView.as_view())
]
