# Generated by Django 2.2.6 on 2019-11-10 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20191109_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='last_reviewed',
            field=models.DateField(auto_now_add=True),
        ),
    ]
