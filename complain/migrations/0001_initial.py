# Generated by Django 2.1.4 on 2019-03-30 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComplainBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('postal', models.CharField(max_length=15)),
                ('phone', models.CharField(max_length=15)),
                ('msg', models.TextField()),
            ],
        ),
    ]
