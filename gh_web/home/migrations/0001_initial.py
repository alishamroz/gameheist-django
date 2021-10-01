# Generated by Django 3.2.6 on 2021-09-09 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamname', models.CharField(max_length=120)),
                ('player1', models.CharField(max_length=120)),
                ('player2', models.CharField(max_length=120)),
                ('player3', models.CharField(max_length=120)),
                ('player4', models.CharField(max_length=120)),
                ('date', models.DateField()),
            ],
        ),
    ]