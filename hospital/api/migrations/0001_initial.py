# Generated by Django 4.0.2 on 2023-06-06 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BLOODBANK',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=10000)),
                ('location', models.CharField(default='', max_length=100)),
                ('a_pve', models.IntegerField(default='', max_length=100)),
                ('a_nve', models.IntegerField(default='', max_length=100)),
                ('ab_nve', models.IntegerField(default='', max_length=100)),
                ('ab_pve', models.IntegerField(default='', max_length=100)),
                ('b_pve', models.IntegerField(default='', max_length=100)),
                ('b_nve', models.IntegerField(default='', max_length=100)),
                ('o_nve', models.IntegerField(default='', max_length=100)),
                ('o_pve', models.IntegerField(default='', max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='HOSPITALS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=10000)),
                ('beds', models.IntegerField(default='', max_length=100)),
                ('icu', models.IntegerField(default='', max_length=100)),
                ('location', models.CharField(default='', max_length=100)),
                ('no_of_doc', models.IntegerField(default='', max_length=100)),
                ('no_of_nurse', models.IntegerField(default='', max_length=100)),
                ('a_pve', models.IntegerField(default='', max_length=100)),
                ('a_nve', models.IntegerField(default='', max_length=100)),
                ('ab_nve', models.IntegerField(default='', max_length=100)),
                ('ab_pve', models.IntegerField(default='', max_length=100)),
                ('b_pve', models.IntegerField(default='', max_length=100)),
                ('b_nve', models.IntegerField(default='', max_length=100)),
                ('o_nve', models.IntegerField(default='', max_length=100)),
                ('o_pve', models.IntegerField(default='', max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='USER',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addhar_no', models.CharField(default='', max_length=10000)),
                ('name', models.CharField(default='', max_length=10000)),
            ],
        ),
    ]