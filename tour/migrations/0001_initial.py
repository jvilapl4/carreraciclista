# Generated by Django 4.2 on 2024-07-02 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=100)),
                ('any_creacio', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Etapa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciutat_origen', models.CharField(max_length=100)),
                ('ciutat_arribada', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ciclista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('edat', models.IntegerField()),
                ('pais', models.CharField(max_length=50)),
                ('equip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ciclistes', to='tour.equip')),
            ],
        ),
    ]
