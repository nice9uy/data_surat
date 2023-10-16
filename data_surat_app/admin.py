from django.contrib import admin

# Register your models here.
from .models import Dbsurat,KatagoriSurat
from .models import KatagoriSurat


admin.site.register(Dbsurat)
admin.site.register(KatagoriSurat)