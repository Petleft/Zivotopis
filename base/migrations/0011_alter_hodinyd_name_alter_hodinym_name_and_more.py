# Generated by Django 4.1.2 on 2022-10-29 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_plath_name_alter_platm_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hodinyd',
            name='name',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='hodinym',
            name='name',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='plath',
            name='name',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='platm',
            name='name',
            field=models.CharField(max_length=10),
        ),
    ]
