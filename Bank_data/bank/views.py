from rest_framework.viewsets import ModelViewSet
from . models import Details
from .serializers import Detailserializer
from itertools import groupby
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.paginator import Paginator
from django_filters.rest_framework.backends import DjangoFilterBackend
from .mypermission import Permission   # only get permisiion is granted to every api


class DetailView(ModelViewSet):   # to get all the branches of a bank
    queryset=Details.objects.all()
    serializer_class=Detailserializer
    permission_classes=[Permission]

    def list(self,request):
        values = [{'bank_name': k, 'branches': list(g)} for k, g in groupby(Details.objects.order_by('bank_name').values(), lambda x: x['bank_name'])]
        pagi=Paginator(values,1)  # to view only 1 bank data at a time as 1 bank data are under same page  so every single value is in different page
        bdetail = request.GET.get('bankdetail')   # getting page from the url get request

        if bdetail==None:   # if we no bank name is provided
            return Response({"msg":"kindly provide bank name for getting its detail"})
        count=1
        for x in values:   # checking requested bank will be in which page as every bank will be in different page
            if x['bank_name']==bdetail:
                break    # i got the bank stop there
            count+=1
        if count==pagi.num_pages+1:  # if requested bank is not found
            return Response({"msg":"bank details not found"})
        products=pagi.page(count)    # get that page  and then return its details
        return Response(products.object_list)  
    
class Getbank(APIView):   # to get all the bank list
    permission_classes=[Permission]

    def get(self,request):
        values = [{'bank_name': k, 'branches': list(g)} for k, g in groupby(Details.objects.order_by('bank_name').values(), lambda x: x['bank_name'])]
        banklist=[x['bank_name'] for x in values]
        return Response(banklist)
    
class Branchdetail(ModelViewSet):   # to get the specific branch
    permission_classes=[Permission]
    queryset=Details.objects.all()
    serializer_class=Detailserializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['bank_name','branch']
