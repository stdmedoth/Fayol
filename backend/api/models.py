# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):

    name = models.CharField(max_length = 200, null=True)
    main_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    wheight = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    supplier = models.CharField(max_length = 200, null=True)
    unit_qnt = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    retail_qnt = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    group = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    observation = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    updated = models.DateTimeField(auto_now = True, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length = 200, null = False)
    doc_type = models.IntegerField(null = False)
    doc_id1 = models.CharField(max_length = 20, null = True)
    doc_id2 = models.CharField(max_length = 20, null = True)
    extern_code = models.CharField(max_length = 20, null = True)
    since = models.DateField(null = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.name
