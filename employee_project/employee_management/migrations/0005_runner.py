# Generated by Django 5.0.1 on 2024-01-16 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_management', '0004_rename_department_id_employee_department_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Runner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('medal', models.CharField(blank=True, choices=[('GOLD', 'Gold'), ('SILVER', 'Silver'), ('BRONZE', 'Bronze')], max_length=10)),
            ],
        ),
    ]
