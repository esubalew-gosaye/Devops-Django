# Generated by Django 4.0.2 on 2022-02-21 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('middle_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('password', models.CharField(max_length=150)),
                ('sex', models.CharField(choices=[('F', 'FEMALE'), ('M', 'Male'), ('O', 'Other')], max_length=10)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('is_counter', models.BooleanField(blank=True, default=False)),
                ('is_admin', models.BooleanField(blank=True, default=False)),
                ('is_costumer', models.BooleanField(blank=True, default=False)),
                ('is_postman', models.BooleanField(blank=True, default=False)),
            ],
        ),
    ]