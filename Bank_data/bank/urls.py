
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router=DefaultRouter()
router.register('bankbranch',views.DetailView,basename='all branch of a bank')
router.register('getbranch',views.Branchdetail,basename='specific branch')
urlpatterns = [
    path('',include(router.urls)),
    path('allbank',views.Getbank.as_view())

]