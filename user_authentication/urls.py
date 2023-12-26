# authentication/urls.py
from django.urls import path
from .views import OwnerViewSet, CustomerViewSet, CustomUserViewSet, AdministratorViewSet, LoginAPIView, AuthorityViewSet

urlpatterns = [
    path('users/', CustomUserViewSet.as_view(), name='user_registration'),
    path('owner/', OwnerViewSet.as_view(), name='owner_registration'),
    path('customer/', CustomerViewSet.as_view(), name='customer_registration'),
    path('admin/', AdministratorViewSet.as_view(), name='admin_reg'),
    path('authority/', AuthorityViewSet.as_view(), name='auth-reg'),
    path('login/', LoginAPIView.as_view(), name='login'),
    # Add more URLs if needed
]
