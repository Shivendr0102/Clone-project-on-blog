# Generated by Django 2.0.3 on 2018-08-05 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180805_1044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='approved_comments',
            new_name='approved_comment',
        ),
    ]
