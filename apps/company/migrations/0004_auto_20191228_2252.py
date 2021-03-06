# Generated by Django 3.0.1 on 2019-12-28 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('localset', '0001_initial'),
        ('company', '0003_auto_20191223_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='netdevices',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='net_devices', to='company.Departments'),
        ),
        migrations.AlterField(
            model_name='netdevices',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='net_devices', to='company.Employee'),
        ),
        migrations.AlterField(
            model_name='netdevices',
            name='host',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='net_devices', to='localset.RegisteredHost'),
        ),
    ]
