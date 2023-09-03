from rest_framework.pagination import PageNumberPagination

class Pages(PageNumberPagination):
    page_size=1

    