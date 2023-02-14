from django.db import models

# Create your models here.
class PayPlan(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)
    
    # 수정 : auto_now=True => 수정 될 때 마다 컬럼 시간 갱신
    # 생성 : auto_now_add=True => 최초 Insert 될 경우만 갱신