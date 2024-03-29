from django.db import models

# Create your models here.
class MfNews(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, blank=True, null=True)
    pubtime = models.BigIntegerField(db_column='pubTime', blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mf_news'