# Generated by Django 3.0 on 2022-12-11 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagetag',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='packagetag_package', to='prog.Package'),
        ),
    ]
