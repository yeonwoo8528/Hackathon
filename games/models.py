from django.db import models


# Create your models here.
class Games(models.Model):
    g_no=models.AutoField(db_column='g_no', primary_key=True)
    g_image = models.CharField(db_column='g_image', max_length=4096)
    g_title= models.CharField(db_column='g_title', max_length=4096)
    g_com = models.CharField(db_column='g_com', max_length=255)
    g_download= models.IntegerField(db_column='g_download', default=0)
    g_age = models.IntegerField(db_column='g_age', default=0)
    g_up = models.CharField(db_column='g_up', max_length=255)
    g_genre=models.CharField(db_column='g_genre', max_length=255)
    g_link = models.CharField(db_column='g_link', max_length=255)
    objects = models.Manager()

    class Meta:
        managed=True
        db_table='games'

    def __str__(self):
        return "이미지 주소: " + self.g_image + ", 제목: " + self.g_title + "회사: "+ self.g_com + "최종 업데이트: "+self.g_up + "게임 링크: "+self.g_link + "게임 장르: " + self.g_genre