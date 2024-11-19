from django.db import models

class Products(models.Model):
    productcode = models.CharField(db_column='productCode', primary_key=True, max_length=10)  # Field name made lowercase.
    name = models.CharField(max_length=50)
    version = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    releasedate = models.DateTimeField(db_column='releaseDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'products'

class Technicians(models.Model):
    techid = models.AutoField(db_column='techID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=50)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=50)  # Field name made lowercase.
    email = models.CharField(unique=True, max_length=50)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'technicians'