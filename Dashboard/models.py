from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from django import forms


# Create your models here.
class Compliance_Matric(models.Model):
    Program_Name = models.CharField(max_length=300)
    

#===========Type Task=====================
    TYPES= (
       ('Document/Program Review', 'Document/Program Review'),
       ('Report Submission', 'Report Submission'),
       ('Inspection', 'Inspection'),
       ('Fee', 'Fee'),
       ('Training', 'Training'),
       ('Permit/License/Registration RenewalTD ', 'Permit/License/Registration RenewalTD '),
        
    )
    Type = models.CharField(max_length=1, choices=TYPES)


#===========FEES REQUIRED=====================

    FEES_REQUIRED= (
        ('Yes', 'Yes'),
        ('No', 'No'),
         
    )
    fee = models.CharField(max_length=200, choices=FEES_REQUIRED)



#===========Regulatory or Non-Regulatory=====================
    CATEGORIES= (
        ('Regulatory', 'Regulatory'),
        ('Non-Regulatory', 'Non-Regulatory'),
            
    )
    category = models.CharField(max_length=50, choices=CATEGORIES)




#===========Physical Record Location=====================Regulatory Submittal Required?

    Record_Location= models.CharField(max_length=300)
    

#===========Regulatory Submittal Required?=====================

    SUBMITTALS_REQUIRED= (
        ('Yes', 'Yes'),
        ('No', 'No'),
         
    )
    Submittal_Required = models.CharField(max_length=50, choices=SUBMITTALS_REQUIRED)


#===========Local Enforcement Agency=====================

    Enforcement_Agency= models.CharField(max_length=300)


#===========BUILDING LOCATION=====================

    BUILDINGS = (
        ('3110', '3110'),
        ('2500', '2500'),
        ('6000', '6000'),
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
    building = models.CharField(max_length=50, choices= BUILDINGS)

#===========TASK=====================

    Task= models.TextField()


#===========FREQUENCY=====================

    FREQUENCIES = (
        ('Monthly', 'Monthly'),
        ('Quarterly', 'Quarterly'),
        ('Semi-Annual', 'Semi-Annual'),
        ('Annual', 'Annual'),
        ('Bienniel', 'Bienniel'),
        ('Trienniel', 'Trienniel'),
        ('Every 5 Years', 'Every 5 Years'),
        ('Quadrennial', 'Quadrennial'),
        ('Quinquennial', 'Quinquennial'),
 

    )
    frequency = models.CharField(max_length=60, choices= FREQUENCIES) 

#===========Resp. EHS Person=========================================

    EHS_PERSONS = (
        ('Doug Fleming', 'Doug Fleming'),
        ('Lenka Barrettova', 'Lenka Barrettova'),
        ('Chris Bradshaw', 'Chris Bradshaw'),
        ('Connie Gordon', 'Connie Gordon'),
        ('Stanley Njoku', 'Stanley Njoku'),
        ('Beverly Everhart', 'Beverly Everhart'),
        ('Kevin Tennyson', 'Kevin Tennyson'),
        ('Mark Kessler', 'Mark Kessler'),
        ('Kimberly Jones', 'Kimberly Jones'),
        ('Jo Schneider', 'Jo Schneider'),
        
    )
    EHS_Person = models.CharField(max_length=300, choices= EHS_PERSONS)


#===========Resp.Functional Person(s)=========================================

    contact_Person = models.CharField (max_length=300)

#===========DUE DATE=====================

    due_Date = models.DateField(null=True)

#===========COMPLETIONS DATE=====================

    Completion_Date = models.DateField(verbose_name='Completion Date')

#===========Permit/Licensing Number=========================================

    Permit_Licensing_Number = models.CharField (max_length=300)
#===========CURENT STATUS=====================

    CURENT_STATUS= (
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Pending Review', 'Pending Review'),
        ('Completed', 'Completed'),
        ('Approved', 'Approved'),
      

    )
    status = models.CharField(max_length=1, choices= CURENT_STATUS) 

# ==============DISPLAYING TABLE INFO
    def __str__(self):
       return'Program_Name:{},Type:{}, Enforcement_Agency:{}, frequency: {}, Type :{}, EHS_Person:{}, category:{}'.format(self.Program_Name, self.Enforcement_Agency, self.frequency, self.Type, self.EHS_Person,self.category)




# 8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888

#====================================EPAS==========================================================================================

# 77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777

class EPAS(models.Model):
    RESPONSIBLE_INDIVIDUAL = (
        ('Stanley Njoku', 'Stanley Njoku'),
        ('Beverly Everhart', 'Beverly Everhart'),
        ('Lenka Barrettova', 'Lenka Barrettova'),
        ('Chris Bradshaw', 'Chris Bradshaw'),
        ('Connie Gordon', 'Connie Gordon'),
        ('Kevin Tennyson', 'Kevin Tennyson'),
    )
    Individual_Responsible = models.CharField(max_length=150, choices= RESPONSIBLE_INDIVIDUAL)

    agency = models.CharField(max_length=200)
   
    description = models.CharField(max_length=30)

    COMPLIANCE_CATEGORY =(
        ('Safety','Safety'),
        ('Environment','Environment'),
        ('Fee',' Fee',),
        ('Regulatory', 'Regulatory'),
        ('Report','Report')
    )
    category = models.CharField(max_length=150, choices = COMPLIANCE_CATEGORY)

# ==============DISPLAYING TABLE INFO============================================
    def __str__(self):
       return'Individual_Responsible:{},agency:{}, description:{}, category: {}'.format(self.Individual_Responsible, self.agency, self.description, self.category)




# 555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555

#==============================FACILITY DATABASE ============================================================================
# ..............................................................................................................................
# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk



class Facility_Database(models.Model):


    Full_Name = models.CharField(max_length=200)
    Title = models.CharField(max_length=200)
    Email_Address = models.EmailField(blank=True, verbose_name ='Email Address')
    Department = models.CharField(max_length=200)
    Phone_number =  models.CharField(max_length=200,)



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
       return'Full_Name:{},Title:{}, Building_Address:{},country: {}, Email_Address:{}'.format(self.Full_Name, self.Title, self.Building_Address, self.country)




