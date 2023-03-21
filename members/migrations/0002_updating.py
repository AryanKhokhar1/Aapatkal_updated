# Generated by Django 4.1.7 on 2023-03-16 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Updating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospitalname', models.CharField(max_length=100)),
                ('hospitaladdress', models.CharField(max_length=100)),
                ('Oxygen1', models.IntegerField()),
                ('Oxygen2', models.IntegerField()),
                ('Oxygen3', models.IntegerField()),
                ('Oxygen4', models.IntegerField()),
                ('Oxygen5', models.IntegerField()),
                ('Oxygen6', models.IntegerField()),
                ('Oxygen7', models.IntegerField()),
                ('Oxygen8', models.IntegerField()),
                ('ebed', models.IntegerField()),
                ('nbed', models.IntegerField()),
                ('ambulance', models.IntegerField()),
                ('Oxygencylinder', models.IntegerField()),
                ('Oxygenvolume', models.IntegerField()),
                ('staffname', models.CharField(max_length=100)),
                ('staffpost', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=25)),
            ],
        ),
    ]
