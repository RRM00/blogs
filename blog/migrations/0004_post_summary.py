# Generated by Django 3.2 on 2021-05-01 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='summary',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
