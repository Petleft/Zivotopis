# Generated by Django 4.1.2 on 2022-11-01 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_typprace_alter_room_typ_práce'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='typ_práce',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
