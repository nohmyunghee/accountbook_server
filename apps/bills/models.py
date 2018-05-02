from django.db import models

# Create your models here.
# 账目表
class Bills(models.Model):
    OUTGO = '0'     # 账目类型.支出
    INCOME = '1'    # 账目类型.收入
    TYPE_CHOICE = (
        (OUTGO, 'OUTGO'),
        (INCOME, 'INCOME'),
    )

    user = models.TextField() # 账目用户ID ForeignKey()
    bill_type = models.CharField(max_length=1, choices=TYPE_CHOICE, default=OUTGO) # 账目类型
    category = models.TextField() # 一级分类ID  
    subcategory = models.TextField() # 二级分类ID
    amount = models.DecimalField(max_digits=16, decimal_places=2, default=0) # 账目金额
    record_date = models.DateField() # 记录时间
    remarks = models.CharField(max_length=140) # 备注 至多140字
    modify_time = models.DateTimeField(auto_now=True) # 修改时间
    create_time = models.DateTimeField(auto_now_add=True) # 创建时间

    class Meta:
        db_table = "bills"
