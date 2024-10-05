from django.db import models


class User_Function(models.TextChoices):
    MANAGER = "Manager", "Manager"
    ENGINEER = "Engineer", "Engineer"
    TECHNICIAN = "Technician", "Technician"
    ADMINISTRATOR = "Administrator", "Administrator"
    SECRETAIRE = "Secretaire", "Secretaire"
    INFORMATICIEN = "Informaticien", "Informaticien"
    COMPTABLE = "Comptable", "Comptable"
    DIRECTEUR = "Directeur", "Directeur"
    

class Departement(models.TextChoices):
    INFORMATIQUE = "Informatique", "Informatique"
    ADMINISTRATION = "Administration", "Administration"
    FINANCE = "Finance", "Finance"
    TECHNIQUE = "Technique", "Technique"
    COMMERCIAL = "Commercial", "Commercial"
    COMMUNICATION = "Communication", "Communication"
    RESSOURCESHUMAIN = "Ressources-Humain", "Ressources-Humain"
    

class Employee(models.Model):
    name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100)
    function = models.CharField(max_length=50, choices=User_Function.choices)
    department = models.CharField(max_length=50, choices=Departement.choices)
    province = models.CharField(max_length=100)
    age = models.IntegerField()
    matricule = models.CharField(max_length=50, unique=True)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.name}"