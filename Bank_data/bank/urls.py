
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router=DefaultRouter()
router.register('bank',views.DetailView,basename='all branch')
router.register('getbranch',views.Branchdetail,basename='specific branch')
urlpatterns = [
    path('',include(router.urls)),
    path('getbank',views.Getbank.as_view())

]