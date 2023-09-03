
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router=DefaultRouter()
router.register('bank',views.DetailView)

urlpatterns = [
    path('',include(router.urls)),
    path('getbank',views.Getbank.as_view())

]