# Generated by Django 4.1.4 on 2023-08-06 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('number', models.IntegerField(verbose_name='Номер')),
                ('courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.courses', verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
                'ordering': ['number'],
            },
        ),
    ]
