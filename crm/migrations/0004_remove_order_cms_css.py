# Generated by Django 4.2.4 on 2023-08-08 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_order_cms_css'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cms_css',
        ),
    ]
