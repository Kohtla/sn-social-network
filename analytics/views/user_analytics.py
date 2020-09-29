from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.serializers import UserSmallSerializer

# /analytics/user
class UserAnalyticsView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        serializer = UserSmallSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)