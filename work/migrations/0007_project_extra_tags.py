# Generated by Django 2.2.1 on 2019-06-06 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0006_auto_20190531_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='extra_tags',
            field=models.CharField(default='', max_length=500, null=True),
        ),
    ]
