# Generated by Django 4.1.4 on 2022-12-15 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_alter_cms_page_page_meta_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='cms_Page',
            new_name='Pages',
        ),
    ]
