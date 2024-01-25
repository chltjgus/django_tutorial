# Generated by Django 5.0.1 on 2024-01-25 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JejuValuePlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emdNM', models.CharField(max_length=100, null=True)),
                ('bsshNm', models.CharField(max_length=200, null=True)),
                ('indutyNm', models.CharField(max_length=200, null=True)),
                ('rnAdres', models.CharField(max_length=200, null=True)),
                ('bsshTelno', models.CharField(max_length=200, null=True)),
                ('prdlstCn', models.CharField(max_length=200, null=True)),
                ('etcCn', models.CharField(max_length=200, null=True)),
                ('regDt', models.CharField(max_length=200, null=True)),
                ('laCrdnt', models.CharField(max_length=200, null=True)),
                ('loCrdnt', models.CharField(max_length=200, null=True)),
                ('dataCd', models.CharField(max_length=200, null=True)),
                ('slctnYr', models.CharField(max_length=200, null=True)),
                ('slctnMm', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]