from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#图书信息
class Book(models.Model):
    book_name=models.CharField(max_length=200)#书名
    book_author=models.CharField(max_length=200)#作者
    book_press=models.CharField(max_length=200)#出版社
    book_price=models.FloatField()#价格
    book_description=models.TextField()#图书介绍
    book_photouri=models.CharField(max_length=500)#图片相对路径  多张图片用!分隔开路径
    remain=models.IntegerField()#图书剩余数量
    def __str__(self):
        return self.book_name
#用户
'''
class User(models.Model):
    user_name=models.CharField(max_length=200)#用户名
    user_email=models.CharField(max_length=20)#用户邮箱
    password=models.CharField(max_length=20)#用户密码
    is_validate=models.BooleanField(default=False)#是否验证
    is_blacklist=models.BooleanField(default=False)#是否在黑名单中
    def __str__(self):
        return self.user_name
'''
# 借阅情况
class Borrow(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)#用户编号
    book_id=models.ForeignKey(Book,on_delete=models.CASCADE)#图书编号
    borrow_time=models.DateTimeField().auto_now#设置为当前时间
    return_time=models.DateTimeField()#还书时间 一本书默认可以借7天
    reborrow_times=models.IntegerField(default=0)#续借次数 默认为0