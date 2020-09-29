from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from datetime import date, timedelta
from dateutil.parser import parse

from posts.models import Like

# /analytics
class LikesAnalyticsView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        date_from = parse(request.GET.get('date_from', ''))
        date_to = parse(request.GET.get('date_to', ''))

        if date_from and date_to:
            count = Like.objects.filter(
                date_created__gte=date_from,
                date_created__lte=date_to
            ).count()

            data = {'count':count}

            return Response(data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


