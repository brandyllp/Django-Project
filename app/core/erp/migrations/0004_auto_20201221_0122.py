# Generated by Django 3.1.4 on 2020-12-21 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0003_remove_employee_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='type',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='erp.type'),
            preserve_default=False,
        ),
    ]
