# Generated by Django 4.1.7 on 2023-02-20 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0008_alter_leaf_object_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaf',
            name='object_count',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
