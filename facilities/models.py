from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from django import forms

# Create your models here.
class FacilityDatabase(models.Model):
    class Meta:
        verbose_name = 'Facilities Database Record'
 

    Full_Name = models.CharField(max_length=200)
    Title = models.CharField(max_length=200)
    Email_Address = models.EmailField(max_length=200, blank=True)
    Department = models.CharField(max_length=200)
    Phone_number = models.CharField(max_length=300)



#================COUNTRY==================================================

    COUNTRIES = (
        ('United States', 'United States'),
        ('Canada', 'Canada'),
        ('Mexico', 'Mexico'),
        ('Brazil', 'Brazil'),
            
    )
    country = models.CharField(max_length=150, choices= COUNTRIES)

#================CITY==================================================

    CITIES = (
        ('Benicia', 'Benicia'),
        ('Billerica', 'Billerica'),
        ('Cambridge', 'Cambridge'),
        ('Grand Junction', 'Grand Junction'),
        ('Hercules', 'Hercules'),
        ('Irvine', 'Irvine'),
        ('Parsippany', 'Parsippany'),
        ('Plano', 'Plano'),
        ('Pleasanton', 'Pleasanton'),
        ('Portland', 'Portland'),
        ('Redmond', 'Redmond'),
        ('Richmond', 'Richmond'),
        ('Santa Rosa', 'Santa Rosa'),
        ('Woodinville', 'Woodinville'),
        ('Distrito Federal', 'Distrito Federal'),
        ('Mississauga', 'Mississauga'),
        ('Saint Laurent', 'Saint Laurent'),
        ('Santa Rosa', 'Santa Rosa'),
        ('Lagoa Santa / Minas Gerais', 'Lagoa Santa / Minas Gerais'),
        ('Sao Paulo', 'Sao Paulo'),


    )
    city = models.CharField(max_length=150, choices= CITIES)

#================BUILDING ADDRESS==================================================

    BUILDIES = (
        ('5400 E. 2nd Street', '5400 E. 2nd Street'),
        ('749 Middlesex Turnpike', '749 Middlesex Turnpike'),
        ('620 Memorial Drive', '620 Memorial Drive'),
        ('2754 Compass Drive', '2754 Compass Drive'),
        ('800 Alfred Nobel Drive', '800 Alfred Nobel Drive'),
        ('825 Alfred Nobel Drive', '825 Alfred Nobel Drive'),
        ('875 Alfred Nobel Drive', '875 Alfred Nobel Drive'),
        ('925 Alfred Nobel Drive', '925 Alfred Nobel Drive'),
        ('1000 Alfred Nobel Drive', '1000 Alfred Nobel Drive'),
        ('2000 Alfred Nobel Drive', '2000 Alfred Nobel Drive'),
        ('4000 Alfred Nobel Drive', '4000 Alfred Nobel Drive'),
        ('6000 James Watson Drive', '6000 James Watson Drive'),
        ('225 LP - Venture', '225 LP - Venture'),
        ('235 LP - Venture', '235 LP - Venture'),
        ('245 LP - Venture', '245 LP - Venture'),
        ('255 LP - Venture', '255 LP - Venture'),
        ('265 LP - Venture', '265 LP - Venture'),
        ('9 Holland Street, Suite 150', '9 Holland Street, Suite 150'),
        ('19 Technology Drive', '19 Technology Drive'),
        ('21 Technology Drive', '21 Technology Drive'),
        ('9500 Jeronimo Road', '9500 Jeronimo Road'),
        ('9560 Jeronimo Road', '9560 Jeronimo Road'),
        ('35 Waterview Blvd.', '35 Waterview Blvd.'),
        ('6000 James Watson Drive', '6000 James Watson Drive'),
        ('2000 Market Street', '2000 Market Street'),
        ('3201 Technology Drive', '3201 Technology Drive'),
        ('5731 West Las Positas', '5731 West Las Positas'),
        ('1045 Riverside Street', '1045 Riverside Street'),
        ('6565 185th Avenue, NE', '6565 185th Avenue, NE'),
        ('2500 Atlas Road (Suite A) Bldg. 2', '2500 Atlas Road (Suite A) Bldg. 2'),
        ('3110 Regatta Boulevard', '3110 Regatta Boulevard'),
        ('487 Aviation Boulevard', '487 Aviation Boulevard'),
        ('14620 NE N. Woodinville Way', '14620 NE N. Woodinville Way'),
        ('8415 - 216th Street, S.E.', '8415 - 216th Street, S.E.'),
        ('35 Waterview Blvd.', '35 Waterview Blvd.'),
        ('Eugenia 197, PGCO 10 A & B', 'Eugenia 197, PGCO 10 A & B'),
        ('1329 Meyerside Drive', '1329 Meyerside Drive'),
        ('3201 Technology Drive', '3201 Technology Drive'),
        ('2403 Rue Guenette Street', '2403 Rue Guenette Street'),
        ('Rua Alfredo Albano da Costa, 100 - Bairro Distrito', 'Rua Alfredo Albano da Costa, 100 - Bairro Distrito'),
        ('Sao Paulo', 'Sao Paulo'),
       

    )
    Building_Address = models.CharField(max_length=150, choices= BUILDIES)

 #=================STATE REGION=============================================================================================

    STATE_REGIONS = (
        ('CA', 'CA'),
        ('CO', 'CO'),
        ('MA', 'MA'),
        ('ME', 'ME'),
        ('NJ', 'NJ'),
        ('ON', 'ON'),
        ('PA', 'PA'),
        ('QC', 'QC'),
        ('TX', 'TX'),
        ('WA', 'WA'),


    )
    State = models.CharField(max_length=150, choices= STATE_REGIONS)


# ==============DISPLAYING TABLE INFO============================================
    def __str__(self):
       return'Full_Name:{},Title:{}, Building_Address:{},country: {}, Email_Address{}'.format(self.Full_Name, self.Title, self.Building_Address, self.country, self.Email_Address)

