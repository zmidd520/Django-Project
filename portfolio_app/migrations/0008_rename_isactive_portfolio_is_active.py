# Generated by Django 4.2.5 on 2023-10-13 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0007_delete_projectsinportfolio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='isActive',
            new_name='is_active',
        ),
    ]
