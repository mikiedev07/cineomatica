from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAdminUser
)

from .models import User, FeedBack, Transaction
from .serializers import UserSerializer, FeedbackSerializer, TransactionSerializer


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
