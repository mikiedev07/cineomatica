from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated,
)

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

    def get_permissions(self):
        """Set custom permissions for each action."""
        if self.action in ["update", "partial_update", "destroy", "list"]:
            self.permission_classes = [
                IsAdminUser,
            ]
        elif self.action in [
            "create",
        ]:
            self.permission_classes = [
                IsAuthenticated,
            ]
        return super().get_permissions()


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

        return Transaction.objects.filter(
            created_at__range=(start_after, end_before), client=self.request.user
        )
