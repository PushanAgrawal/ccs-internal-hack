# Generated by Django 4.0.2 on 2023-06-06 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DISTANCE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hid', models.IntegerField()),
                ('dist', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MEDICINE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=1000)),
                ('hospital', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AddField(
            model_name='user',
            name='blood_group',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AddField(
            model_name='user',
            name='curr_location',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AlterField(
            model_name='bloodbank',
            name='a_nve',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bloodbank',
            name='a_pve',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bloodbank',
            name='ab_nve',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bloodbank',
            name='ab_pve',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bloodbank',
            name='b_nve',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bloodbank',
            name='b_pve',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bloodbank',
            name='o_nve',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bloodbank',
            name='o_pve',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='hospitals',
            name='a_nve',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='hospitals',
            name='a_pve',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='hospitals',
            name='ab_nve',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='hospitals',
            name='ab_pve',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='hospitals',
            name='b_nve',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='hospitals',
            name='b_pve',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='hospitals',
            name='beds',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='hospitals',
            name='icu',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='hospitals',
            name='no_of_doc',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='hospitals',
            name='no_of_nurse',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='hospitals',
            name='o_nve',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='hospitals',
            name='o_pve',
            field=models.IntegerField(default=0),
        ),
    ]