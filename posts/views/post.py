from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from posts.serializers import PostSerializer


# /posts
class PostView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        serializer = PostSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            request.user.update_last_action()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)