# Generated by Django 3.1.8 on 2021-10-28 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20211028_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]