from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.core.exceptions import ObjectDoesNotExist

from posts.serializers import LikeSerializer
from posts.models import Post, Like


class LikeView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, **kwargs):
        try:
            post = Post.objects.get(id=kwargs['post'])
            like, created = Like.objects.get_or_create(post=post, user=request.user)
            if created:
                like.save()
            serializer = LikeSerializer(like)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, **kwargs):
        post = Post.objects.get(id=kwargs['post'])
        Like.objects.get(user=request.user, post=post).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


