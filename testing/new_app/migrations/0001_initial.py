# Generated by Django 3.2 on 2021-04-28 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient_info',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('mail', models.EmailField(default=None, max_length=254)),
                ('xray_sheet', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
