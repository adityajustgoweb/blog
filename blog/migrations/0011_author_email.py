# Generated by Django 4.1.4 on 2022-12-19 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_post_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='email',
            field=models.CharField(default='test@gmail.com', max_length=30),
        ),
    ]