from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from posts.serializers import LikeSerializer


class LikeView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        pass

    def delete(self, request):
        pass
