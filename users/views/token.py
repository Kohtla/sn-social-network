from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import update_last_login
from users.models import User


class CustomTokenObtainPairView(TokenObtainPairView):

    def post(self, request):
        response = super(TokenObtainPairView, self).post(request)
        try:
            user = User.objects.get(username=request.data['username'])
            update_last_login(None, user)
        except:
            return None
        return response
