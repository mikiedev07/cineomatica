from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from rest_framework.generics import ListAPIView
from django.views.generic.list import ListView
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAdminUser
)

from django_filters import rest_framework as filters
from .filters import TransactionFilter
from .models import User, FeedBack, Transaction
from .serializers import (
    UserSerializer,
    FeedbackSerializer,
    TransactionSerializer,
    HistorySerializer,
)


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]


class FeedbackViewSet(ModelViewSet):
    serializer_class = FeedbackSerializer
    queryset = FeedBack.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


class TransactionViewSet(ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    permission_classes = [IsAdminUser]


class HistoryView(ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = HistorySerializer

    def get_queryset(self):
        start_after = self.request.data.get("start_after")
        end_before = self.request.data.get("end_before")
        print(start_after, end_before)

        return Transaction.objects.filter(created_at__range=(start_after, end_before))

# {
#     "start_date": "2020-12-12 10:10:10",
#     "end_date": "2020-12-24 10:10:10"
# }
