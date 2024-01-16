# Generated by Django 5.0.1 on 2024-01-16 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_management', '0008_topping_pizza'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission_name', models.CharField(max_length=203)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='permission',
            field=models.ManyToManyField(to='employee_management.permission'),
        ),
        migrations.DeleteModel(
            name='Pizza',
        ),
        migrations.DeleteModel(
            name='Topping',
        ),
    ]
