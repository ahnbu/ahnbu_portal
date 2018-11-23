from django.db import models
from django.utils import timezone

import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse

# Create your models here.


class Price(models.Model):
    name = models.CharField(max_length=50)
    summary = models.TextField()
    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    discount_price = models.PositiveIntegerField(blank=True, default=0)
    category = models.CharField(max_length=20)
    link = models.TextField()
    update_date = models.DateTimeField()

#    is_publish = models.BooleanField(default = False)
# 정렬조건 지정 위 class 하위로 지정해야 함. 같은 레벨 아님 !!

    class Meta:
        ordering = ['-update_date', '-id']  # ==> desc로 정렬

    def __str__(self):
        return f'{self.name}, {self.discount}'
