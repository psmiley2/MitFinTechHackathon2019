# Generated by Django 2.2.6 on 2019-11-10 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_questions_investment_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='beta',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
    ]