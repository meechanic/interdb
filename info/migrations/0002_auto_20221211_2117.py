# Generated by Django 3.0 on 2022-12-11 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infsourcetag',
            name='infsource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='infsourcetag_infsource', to='info.Infsource'),
        ),
    ]
