# Generated by Django 4.2.6 on 2023-10-14 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dbsurat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('surat', models.CharField(max_length=10)),
                ('kategori', models.CharField(max_length=30)),
                ('tgl', models.DateField()),
                ('no_surat', models.CharField(max_length=200)),
                ('kepada', models.CharField(max_length=200)),
                ('perihal', models.CharField(max_length=200)),
                ('upload_file', models.FileField(upload_to='')),
            ],
            options={
                'db_table': 'Dbsurat',
            },
        ),
        migrations.CreateModel(
            name='KatagoriSurat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('katagori', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Katagori',
            },
        ),
    ]