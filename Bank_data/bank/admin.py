from django.contrib import admin
from .models import Details

@admin.register(Details)
class DetailRegister(admin.ModelAdmin):
    list_display=['id','ifsc','bank_id','city']
