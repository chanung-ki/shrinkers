from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
class PayPlan(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)
    
    # 수정 : auto_now=True => 수정 될 때 마다 컬럼 시간 갱신
    # 생성 : auto_now_add=True => 최초 Insert 될 경우만 갱신
    
    
# User table 생성
# 총 방법 두가지

# 1번 
# 테이블 하나에 쌓임
class Users(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    join_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    # pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING)
    

# 2번
# 테이블 두개에 쌓임
# class UserDetail(models.Model):
#     user= models.OneToOneField(Users, on_delete=models.CASCADE)
#     pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING)

# OneToOneField => 1대1 매핑이 되도록 하게 하겠다.