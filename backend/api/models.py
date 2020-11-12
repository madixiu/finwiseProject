from django.db import models


# Create your models here.
# class firm(models.Model):
#     ID = models.IntegerField(primary_key=True)
#     ticker = models.CharField(max_length=100)
#     name = models.CharField(max_length=200)
#     desc = models.TextField()
#     enabled = models.BooleanField()
#     market = models.IntegerField()
#     industry = models.IntegerField()
#     created = models.DateTimeField()
#     updated = models.DateTimeField()
#     tseEngName = models.CharField(max_length=200)
#     tseEngTicker = models.CharField(max_length=100)
#     tse12digitCode = models.CharField(max_length=30)
#     tse5digitCode = models.CharField(max_length=20)
#     tickerfull = models.CharField(max_length=100)
#     urlParameter = models.CharField(max_length=100)
#     company12digitCode = models.CharField(max_length=20)
#     company4character = models.CharField(max_length=10)

#     class Meta:
#         managed = False
#         db_table = 'firm'


# class market(models.Model):
#     ID = models.IntegerField()
#     name = models.CharField(max_length=100)
#     engName = models.CharField(max_length=100)
