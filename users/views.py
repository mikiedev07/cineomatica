from rest_framework.viewsets import ModelViewSet

from .models import User, FeedBack, Transaction
from .serializers import UserSerializer, FeedbackSerializer, TransactionSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class FeedbackViewSet(ModelViewSet):
    serializer_class = FeedbackSerializer
    queryset = FeedBack.objects.all()


class TransactionViewSet(ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
