from django.db import models
from django.utils import timezone

# Create your models here.

class PersionInfo(models.Model):
    """
    用户个人信息
    """
    name = models.CharField(max_length=128, default='', verbose_name="姓名")
    phone = models.CharField(max_length=32, default='', verbose_name="手机号")
    profession = models.CharField(max_length=128, default='', verbose_name="专业班级")
    school = models.CharField(max_length=128, default='', verbose_name="学校")
    principal = models.CharField(max_length=128, default='', verbose_name="上级负责人")
    add_time = models.DateTimeField(default=timezone.now, verbose_name="提交时间")
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "个人信息"
        verbose_name_plural = verbose_name
        ordering = ["-add_time"]