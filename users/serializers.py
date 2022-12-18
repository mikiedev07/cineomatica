from rest_framework.serializers import ModelSerializer
from .models import (
    User,
    FeedBack,
    Transaction,
)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data["email"], name=validated_data["name"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = FeedBack
        fields = "__all__"


class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"


class HistorySerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = ("created_at", "discount", "total", "movie_name")
