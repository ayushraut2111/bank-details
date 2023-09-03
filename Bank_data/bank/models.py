from django.db import models

class Details(models.Model):
    ifsc=models.CharField(max_length=50)
    bank_id=models.IntegerField()
    branch=models.CharField(max_length=100)
    address=models.TextField()
    city=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    bank_name=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.ifsc
