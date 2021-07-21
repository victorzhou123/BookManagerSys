# Generated by Django 3.2.5 on 2021-07-21 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32)),
                ('price', models.FloatField(max_length=10)),
                ('date', models.DateField()),
                ('publish', models.CharField(max_length=32)),
            ],
        ),
    ]