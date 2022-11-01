# Generated by Django 4.1.2 on 2022-11-01 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_alter_room_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='typprace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='room',
            name='typ_práce',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.typ'),
        ),
    ]
