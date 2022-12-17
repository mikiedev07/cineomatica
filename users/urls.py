from rest_framework import routers
from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    UserViewSet,
    FeedbackViewSet,
    TransactionViewSet,
)
from .views import HistoryView

app_name = "users"

router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('feedbacks', FeedbackViewSet)
router.register('transactions', TransactionViewSet)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('history/', HistoryView.as_view(), name='user_purchases')
]

urlpatterns += router.urls

