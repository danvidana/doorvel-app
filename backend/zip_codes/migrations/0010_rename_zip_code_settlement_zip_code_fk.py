# Generated by Django 4.1.7 on 2023-03-05 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zip_codes', '0009_alter_settlement_key'),
    ]

    operations = [
        migrations.RenameField(
            model_name='settlement',
            old_name='zip_code',
            new_name='zip_code_fk',
        ),
    ]
