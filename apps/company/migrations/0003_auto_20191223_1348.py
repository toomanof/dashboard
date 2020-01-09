# Generated by Django 3.0.1 on 2019-12-23 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_employee_host'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='host',
        ),
        migrations.CreateModel(
            name='NetDevices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Имя')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='company.Employee')),
                ('host', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='company.Departments')),
            ],
        ),
    ]