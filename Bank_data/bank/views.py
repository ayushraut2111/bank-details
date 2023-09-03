from rest_framework.viewsets import ModelViewSet
from . models import Details
from .serializers import Detailserializer
from itertools import groupby
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.paginator import Paginator
from .mypermission import Permission   # only get permission is granted to every api


class DetailView(ModelViewSet):   # to get all the branches of specific bank
    queryset=Details.objects.all()
    serializer_class=Detailserializer
    permission_classes=[Permission]

    def list(self,request):
        values = [{'bank_name': k, 'branches': list(g)} for k, g in groupby(Details.objects.order_by('bank_name').values(), lambda x: x['bank_name'])]
        pagi=Paginator(values,1)  # to view only 1 bank data at a time as 1 bank data are under same page  so every single value is in different page
        bdetail = request.GET.get('bank_name')   # getting page from the url get request

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
    
    
class Branchdetail(ModelViewSet):   # to get the specific branch of a bank
    permission_classes=[Permission]
    queryset=Details.objects.all()
    serializer_class=Detailserializer
    def list(self,request):
        bank=request.GET.get('bank_name')
        branch=request.GET.get('branch')
        print(bank,branch)
        if bank and branch:
            if Details.objects.filter(bank_name=bank,branch=branch).exists():
                obj=Details.objects.filter(bank_name=bank,branch=branch)
                # print(obj)
                ser=Detailserializer(obj,many=True)
                return Response(ser.data)
            else:
                return Response({"msg":"please enter valid bank name or branch name"})
        else:
            return Response({"msg":"please enter bank and branch name to get the details"})
        


class Getbank(APIView):   # to get all the bank list
    permission_classes=[Permission]

    def get(self,request):
        values = [{'bank_name': k, 'branches': list(g)} for k, g in groupby(Details.objects.order_by('bank_name').values(), lambda x: x['bank_name'])]
        banklist=[x['bank_name'] for x in values]
        return Response(banklist)