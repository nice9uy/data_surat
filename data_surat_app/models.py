from django.db import models

# Create your models here.

class Dbsurat(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    surat = models.CharField(max_length=10)
    kategori = models.CharField(max_length=30)
    tgl = models.DateField()
    no_surat = models.CharField(max_length=200)
    kepada = models.CharField(max_length=200)
    perihal = models.CharField(max_length=200)
    upload_file = models.FileField(upload_to='')
 
    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table = "Dbsurat"

class KatagoriSurat (models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    katagori = models.CharField(max_length=30)

    class Meta:
        db_table = "Katagori"