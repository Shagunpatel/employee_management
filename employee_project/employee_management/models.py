from django.db import models
from django.urls import reverse
# Create your models here.
class Department(models.Model):
    Department_Id=models.IntegerField(primary_key=True)
    Department_Name=models.CharField(max_length=256)
    Description=models.TextField()
    def __str__(self):
        return self.Department_Name

class Position(models.Model):
    Position_Id=models.IntegerField(primary_key=True)
    Position_Name=models.CharField(max_length=256)
    Description=models.TextField()
    def __str__(self):
        return self.Position_Name

class Permission(models.Model):
    permission_name=models.CharField(max_length=203)
    def __str__(self):
        return self.permission_name
class Employee(models.Model):
    gender_choices=[("F","Female"),("M","Male"),("O","Others")]
    Employee_Id=models.IntegerField(primary_key=True)
    First_Name=models.CharField(max_length=256)
    Last_Name=models.CharField(max_length=256)
    Gender=models.CharField(max_length=1,choices=gender_choices)
    Salary=models.PositiveIntegerField()
    Department=models.ForeignKey(Department,on_delete=models.CASCADE)
    Position=models.ForeignKey(Position,on_delete=models.CASCADE)
    Location=models.CharField(max_length=256)
    Phone_No=models.BigIntegerField()
    Date_Of_Joining=models.DateField()
    permission=models.ManyToManyField(Permission)

    def __str__(self):
        return self.First_Name
    

    def get_absolute_url(self):
        return reverse("emp:view")
    
# class Runner(models.Model):
#     MedalType = models.TextChoices("MedalType", "GOLD SILVER BRONZE")
#     name = models.CharField(max_length=60)
#     medal = models.CharField(blank=True, choices=MedalType, max_length=10)

# class Topping(models.Model):
#     topping_name=models.CharField(max_length=230)
#     def __str__(self):
#         return self.topping_name


# class Pizza(models.Model):
    # ...
    # toppings = models.ManyToManyField(Topping)
    




