# Generated by Django 3.0.1 on 2020-01-09 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('localset', '0001_initial'),
        ('company', '0004_auto_20191228_2252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите назваине', max_length=250, verbose_name='Название')),
            ],
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='departments',
            new_name='department',
        ),
        migrations.AddField(
            model_name='employee',
            name='nickname',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Обращение'),
        ),
        migrations.AlterField(
            model_name='departments',
            name='name',
            field=models.CharField(help_text='Введите назваине', max_length=250, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='netdevices',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='net_devices', to='company.Departments', verbose_name='Отдел'),
        ),
        migrations.AlterField(
            model_name='netdevices',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='net_devices', to='company.Employee', verbose_name='Сотрудник'),
        ),
        migrations.AlterField(
            model_name='netdevices',
            name='host',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='net_devices', to='localset.RegisteredHost', verbose_name='Зарегистрированный хост'),
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='company.Position'),
        ),
    ]
