# Generated by Django 3.2 on 2021-06-02 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210602_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='country_code',
            field=models.CharField(default='+91', max_length=5),
        ),
    ]
