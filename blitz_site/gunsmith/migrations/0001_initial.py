# Generated by Django 4.1.7 on 2023-03-19 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='WeaponReceiver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('category', models.CharField(choices=[('AR', 'Assault Rifle'), ('BR', 'Battle Rifle'), ('SMG', 'Submachine Gun'), ('LMG', 'Light Machine Gun'), ('SHT', 'Shotgun'), ('MRK', 'Marksman Rifle'), ('SNI', 'Sniper Rifle'), ('MEL', 'Melee'), ('HND', 'Handgun'), ('LAU', 'Launcher')], default='AR', max_length=3)),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receivers', to='gunsmith.platform')),
            ],
        ),
    ]
