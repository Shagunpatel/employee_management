# Generated by Django 5.0.1 on 2024-01-11 12:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('Department_Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Department_Name', models.CharField(max_length=256)),
                ('Description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('Poition_Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Position', models.CharField(max_length=256)),
                ('Description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Employee_Id', models.IntegerField(primary_key=True, serialize=False)),
                ('First_Name', models.CharField(max_length=256)),
                ('Last_Name', models.CharField(max_length=256)),
                ('Salary', models.PositiveIntegerField()),
                ('Location', models.CharField(max_length=256)),
                ('Phone_No', models.BigIntegerField()),
                ('Date_Of_Joining', models.DateField()),
                ('Department_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_management.department')),
                ('Position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_management.position')),
            ],
        ),
    ]
