# Generated by Django 5.0 on 2023-12-26 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.BigIntegerField()),
                ('details', models.CharField(max_length=150)),
                ('cat', models.CharField(max_length=50)),
            ],
        ),
    ]