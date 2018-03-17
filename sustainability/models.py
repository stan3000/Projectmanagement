from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from django import forms
# Create your models here.


class SustainableReport(models.Model):
    data_Recorded_By = models.CharField(max_length=50)
    account_No = models.CharField(max_length=70)

    BUILDINGS = (
        ('3110 Regatta Bvld', '3110 Regatta Bvld'),
        ('2500 Atlas Rd', '2500 Atlas Rd'),
        ('6000 James Watson Dr', '6000 James Watson Dr'),
        ('4000', '4000'),
        ('2000', '2000'),
        ('800', '800'),
        ('825', '825'),
        ('875', '875'),
        ('925', '925'),
        ('1000', '1000'),
        ('225', '225'),
        ('235', '235'),
        ('245', '245'),
        ('255', '255'),
        ('265', '265'),
        ('800', '800'),
        ('825', '825'),
        ('875', '875'),
        ('925', '925'),
        ('5731', '5731'),
        ('487', '487'),
        ('5400', '5400'),
        ('5500', '5500'),
    )
    building = models.CharField(max_length=100, choices =BUILDINGS)

#===========CITY=====================

    CITIES = (
        ('Hercules', 'Hercules'),
        ('Richmond', 'Richmond'),
        ('Santa Rosa', 'Santa Rosa'),
        ('Pleasanton', 'Pleasanton'),
        ('Benicia', 'Benicia'),
    
    )
    city = models.CharField(max_length=100, choices=CITIES)

#===========Region=====================
    REGIONS = (
        ('NorCal', 'NorCal'),
        ('NorWest', 'NorWest'),
        ('APAC', 'APAC'),
        ('Europe', 'Europe'),
            
    )
    region = models.CharField(max_length=100, choices=REGIONS)



#===========Type Consumped=====================
    TYPES= (
        ('Electricity', 'Electricity'),
        ('Gas', 'Gas'),
        ('Therms', 'Therms'),
        ('Water', 'Water'),
       
    )
    Type = models.CharField(max_length=100, choices=TYPES)


#======== CATEGORY==========================


    CATEGORY_STATEMENTS= (
         ('Monthly Statement', 'Monthly Statement'),
         ('Quarterly Statement', 'Quarterly Statement'),
         ('Annual Statement','Annual Statement'),
         
     )
    category = models.CharField(max_length=150, choices=CATEGORY_STATEMENTS)

#======Consumped===========================
    Amount_Consumped = models.CharField(max_length=200)
    Amount_Spent = models.CharField(max_length=200)

#===========UNIT TYPE=====================
    UNITS= (
        ('kWh', 'kWh'),
        ('Therms', 'Therms'),
        ('Gallons', 'Gallons'),
       
    )
    unit = models.CharField(max_length=100, choices=UNITS)


#===========Year=====================

    Billing_Period_Start_Date = models.DateField()

    Billing_Period_End_Date = models.DateField()


#==========REPORTING STATUS=================================

    SUSTAINABILITY_REPORTING_STATUS = (
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Pending Review', 'Pending Review',),
        ('On Hold', 'On Hold'),
        ('Approved', 'Approved'),
        ('Completed', 'Completed'),
    )
    status = models.CharField(max_length=150, choices=SUSTAINABILITY_REPORTING_STATUS)



    comment = models.TextField()

# ==============DISPLAYING TABLE INFO
    def __str__(self):
       return'data_Recorded_By:{},building:{}, city:{}, region: {}, Type :{}, Amount_Consumped:{}, unit:{}'.format(self.data_Recorded_By, self.building, self.city, self.region, self.Type, self.Amount_Consumped,self.unit)
