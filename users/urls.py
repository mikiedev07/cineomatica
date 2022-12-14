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

app_name = "users"

router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('feedbacks', FeedbackViewSet)
router.register('transactions', TransactionViewSet)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls
