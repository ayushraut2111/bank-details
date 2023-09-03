from rest_framework.viewsets import ModelViewSet
from . models import Details
from .serializers import Detailserializer
from itertools import groupby
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.paginator import Paginator


class DetailView(ModelViewSet):
    queryset=Details.objects.all()
    serializer_class=Detailserializer

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
    
class Getbank(APIView):
    def get(self,request):
        values = [{'bank_name': k, 'branches': list(g)} for k, g in groupby(Details.objects.order_by('bank_name').values(), lambda x: x['bank_name'])]
        banklist=[x['bank_name'] for x in values]
        return Response(banklist)

    

    

