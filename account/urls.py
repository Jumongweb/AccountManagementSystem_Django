from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register('accounts', views.AccountViewSet)

urlpatterns = [
    # path('accounts/', views.ListAccount.as_view()),
    # path('accounts/get/<int:pk>/', views.AccountDetail.as_view()),
    path('', include(router.urls)),
    path('deposit/', views.deposit),
    path('withdraw/', views.withdraw),
    # path('create', views.createAccount.as_view())
]