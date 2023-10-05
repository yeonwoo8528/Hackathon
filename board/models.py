from django.db import models

# Create your models here.
from django.db import models
from games.models import Games
class Board(models.Model):

    b_no=models.IntegerField(db_column='b_no',primary_key=True)
    b_age=models.IntegerField(db_column='b_age',default=0)
    b_sex = models.CharField(db_column='b_sex', max_length=50)
    b_genre = models.CharField(db_column='b_genre', max_length=50)
    b_time = models.CharField(db_column='b_time', max_length=20)
    objects = models.Manager()


    class Meta:
        managed = True
        db_table = 'board'

    def __str__(self):
        return "성별: " + self.b_sex + ", 장르: " + self.b_genre + "시간: "+ self.b_time

