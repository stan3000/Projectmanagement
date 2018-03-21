from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from django import forms


# Create your models here.
class ComplianceMatric(models.Model):
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
    Type = models.CharField(max_length=100, choices=TYPES)


#===========FEES REQUIRED=====================

    FEES_REQUIRED= (
        ('Yes', 'Yes'),
        ('No', 'No'),
         
    )
    fee = models.CharField(max_length=100, choices=FEES_REQUIRED)



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
    building_Number = models.CharField(max_length=50, choices= BUILDINGS)

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




    #===========BUILDING LOCATION=====================

    BUILDINGS = (
        ('3110 Regatta', '3110 Regatta'),
        ('2500 Atlas', '2500 Atlas'),
        ('6000 James Watson', '6000 James Watson'),
        ('4000 Alfred Nobel', '4000 Alfred Nobel'),
        ('2000 Alfred Nobel', '2000 Alfred Nobel'),
        ('800 Alfred Nobel', '800 Alfred Nobel'),
        ('825 Alfred Nobel', '825 Alfred Nobel'),
        ('875 Alfred Nobel', '875 Alfred Nobel'),
        ('925 Alfred Nobel', '925 Alfred Nobel'),
        ('1000 Alfred Nobel', '1000 Alfred Nobel'),
        ('225 Linus Pauling', '225 Linus Pauling'),
        ('235 Linus Pauling', '235 Linus Pauling'),
        ('245 Linus Pauling', '245 Linus Pauling'),
        ('255 Linus Pauling', '255 Linus Pauling'),
        ('265 Linus Pauling', '265 Linus Pauling'),
        ('5731 W. Las Positas', '5731 W. Las Positas'),
        ('487 Aviation Boulevard', '487 Aviation Boulevard'),
        ('5400 E. 2nd St', '5400 E. 2nd St'),
        ('5500 E. 2nd St', '5500 E. 2nd St'),


    )
    building= models.CharField(max_length=50, choices= BUILDINGS)



#===========Resp.Functional Person(s)=========================================

    contact_Person = models.CharField (max_length=300)

#===========DUE DATE=====================

    due_Date = models.DateField(null=True)

#===========COMPLETIONS DATE=====================

    Completion_Date = models.DateField()

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
    status = models.CharField(max_length=100, choices= CURENT_STATUS) 

# ==============DISPLAYING TABLE INFO
    def __str__(self):
       return'Program_Name:{}, building{}, Type:{}, Enforcement_Agency:{}, frequency: {}, EHS_Person:{}, category:{}'.format(self.Program_Name, self.building, self.Enforcement_Agency, self.frequency, self.Type, self.EHS_Person,self.category)


# 55555555555555555555555555555555555555555555555555555555555555555555555
#========EPAS TRACKER==================================================
# 3232333333333333333333333333333333333333333333333333333333333333333

class EHSProjectApplicabliltyStatusReport(models.Model):
    
    RESPONSIBLE_INDIVIDUAL = (
        ('Stanley Njoku', 'Stanley Njoku'),
        ('Beverly Everhart', 'Beverly Everhart'),
        ('Lenka Barrettova', 'Lenka Barrettova'),
        ('Chris Bradshaw', 'Chris Bradshaw'),
        ('Connie Gordon', 'Connie Gordon'),
        ('Kevin Tennyson', 'Kevin Tennyson'),
    )
    Individual_Responsible = models.CharField(max_length=150, choices= RESPONSIBLE_INDIVIDUAL)


    BUILDINGS = (
        ('3110 Regatta', '3110 Regatta'),
        ('2500 Atlas', '2500 Atlas'),
        ('6000 James Watson', '6000 James Watson'),
        ('4000 Alfred Nobel', '4000 Alfred Nobel'),
        ('2000 Alfred Nobel', '2000 Alfred Nobel'),
        ('800 Alfred Nobel', '800 Alfred Nobel'),
        ('825 Alfred Nobel', '825 Alfred Nobel'),
        ('875 Alfred Nobel', '875 Alfred Nobel'),
        ('925 Alfred Nobel', '925 Alfred Nobel'),
        ('1000 Alfred Nobel', '1000 Alfred Nobel'),
        ('225 Linus Pauling', '225 Linus Pauling'),
        ('235 Linus Pauling', '235 Linus Pauling'),
        ('245 Linus Pauling', '245 Linus Pauling'),
        ('255 Linus Pauling', '255 Linus Pauling'),
        ('265 Linus Pauling', '265 Linus Pauling'),
        ('5731 W. Las Positas', '5731 W. Las Positas'),
        ('487 Aviation Boulevard', '487 Aviation Boulevard'),
        ('5400 E. 2nd St', '5400 E. 2nd St'),
        ('5500 E. 2nd St', '5500 E. 2nd St'),
        ('All NorCal Sites', 'All NorCal Sites'),

    )
    building = models.CharField(max_length=300, choices= BUILDINGS )
 


    EHS_PROGRAMS = (
        ('Accident Investigation / Injury Reporting', 'Accident Investigation / Injury Reporting'),
        ('Air Quality - (BAAQMD / SCAQD etc)', 'Air Quality - (BAAQMD / SCAQD etc)'),
        ('Asbestos', 'Asbestos'),
        ('Biosafety (BSO)', 'Biosafety (BSO)'),
        ('Bloodborne Pathogens', 'Bloodborne Pathogens'),
        ('Chemges / Evo / SDS generation', 'Chemges / Evo / SDS generation'),
        ('Chemical Management', 'Chemical Management'),
        ('Chemical Hygiene Plan', 'Chemical Hygiene Plan'),
        ('Chemtrec', 'Chemtrec'),
        ('Cold Work', 'Cold Work'),
        ('Compressed Gas and Compressed Air', 'Compressed Gas and Compressed Air'),
        ('Confined Space', 'Confined Space'),
        ('Contractor Safety', 'Contractor Safety'),
        ('Cranes, Hoists, Lifts', 'Cranes, Hoists, Lifts'),
        ('DOT / IATA / DG', 'DOT / IATA / DG'),
        ('EHS Training Program Managment', 'EHS Training Program Managment'),
        ('Electrical Safety', 'Electrical Safety'),
        ('Emergency Action Plan (EAP)', 'Emergency Action Plan (EAP)'),
        ('Emergency Eyewash and Shower', 'Emergency Eyewash and Shower'),
        ('Ergonomics - Industrial', 'Ergonomics - Industrial'),
        ('Ergonomics - Office', 'Ergonomics - Office'),
        ('ERT MERT', 'ERT MERT'),
        ('ERT HazMat', 'ERT HazMat'),
        ('Field Service Safety', 'Field Service Safety'),
        ('Fire Protection', 'Fire Protection'),
        ('Fleet Safety', 'Fleet Safety'),
        ('Hand and Portable Power Tools', 'Hand and Portable Power Tools'),
        ('Hazardous Communication (HazCom)', 'Hazardous Communication (HazCom)'),
        ('Hazardous Materials Business Plan (HMBP)', 'Hazardous Materials Business Plan (HMBP)'),
        ('Hearing Conservation', 'Hearing Conservation'),
        ('Hazardous Waste Mgmt', 'Hazardous Waste Mgmt'),
        ('Industrial Hygiene Program', 'Industrial Hygiene Program'),
        ('Industrial Wastewater', 'Industrial Wastewater'),
        ('Injury and Illness Prevention Program (IIPP) - California Only', 'Injury and Illness Prevention Program (IIPP) - California Only'),
        ('Laser Safety (LSO)', 'Laser Safety (LSO)'),
        ('Local Exhaust Ventilation', 'Local Exhaust Ventilation'),
        ('Lockout Tagout LOTO', 'Lockout Tagout LOTO'),
        ('Machine Guarding', 'Machine Guarding'),
        ('Medical and First Aid', 'Medical and First Aid'),
        ('Medical Surveillance', 'Medical Surveillance'),
        ('Medical Waste', 'Medical Waste'),
        ('New Hire Orientation', 'New Hire Orientation'),
        ('OSHA 300', 'OSHA 300'),
        ('OSHA IH Testing', 'OSHA IH Testing'),
        ('Powered Industrial Trucks', 'Powered Industrial Trucks'),
        ('Powered Platforms', 'Powered Platforms'),
        ('PPE/JHA', 'PPE/JHA'),
        ('Pressure Vessels / Boilers', 'Pressure Vessels / Boilers'),
        ('Radiation Safety', 'Radiation Safety'),
        ('Record Keeping', 'Record Keeping'),
        ('Refrigeration Management Program (RMP)', 'Refrigeration Management Program (RMP)'),
        ('Remediation', 'Remediation'),
        ('Respiratory Protection', 'Respiratory Protection'),
        ('Safety Committee', 'Safety Committee'),
        ('SDS Management (SDS-Pro)', 'SDS Management (SDS-Pro)'),
        ('SPCC', 'SPCC'),
        ('Stormwater', 'Stormwater'),
        ('OSHA IH Testing', 'OSHA IH Testing'),
        ('Toxic Release Inventory (TRI)', 'Toxic Release Inventory (TRI)'),
        ('TSCA', 'TSCA'),
        ('Walking and Working Surfaces', 'Walking and Working Surfaces'),
        ('Waste Minimization', 'Waste Minimization'),
        ('Welding Cutting Brazing (Hot Work)', 'Welding Cutting Brazing (Hot Work)'),
        ('Workers Comp', 'Workers Comp'),
        ('Working Alone', 'Working Alone'),
        ('Working at Heights', 'Working at Heights'),


    )
    Program = models.CharField(max_length=300, choices= EHS_PROGRAMS)


#===========TYPE=====================================================================

    TYPES= (
        ('Environmental', 'Environmental'),
        ('Safety', 'Safety'),
        ('Fees', 'Fees'),
        ('Report', 'Report'),
        ('Permit/License', 'Permit/License'),
             

    )
    Type = models.CharField(max_length=100, choices= TYPES)



#===========CATEGORIES=====================================================================

    CATEGORIES= (
        ('Local Agency', 'Local Agency'),
        ('EPA', 'EPA'),
        ('State', 'State'),
        ('City', 'City'),
        ('OSHA', 'OSHA'),
        ('County', 'County'),
             

    )
    category = models.CharField(max_length=50, choices= CATEGORIES)



#===========Site Applicability=====================

    SITE_APPLICABILITIES= (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('N/A', 'N/A'),
        ('Pending Verification', 'Pending Verification'),
             

    )
    Site_Applicability = models.CharField(max_length=50, choices= SITE_APPLICABILITIES)




#===========RANKING=====================

    RANKINGS= (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
                

    )
    Ranking = models.CharField(max_length=200, choices= RANKINGS)




#===========Program in place?=====================

    PROGRAMS_IN_PLACE= (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('N/A', 'N/A'),
        ('Pending Verification', 'Pending Verification'),
             

    )
    Program_in_Place = models.CharField(max_length=100, choices= PROGRAMS_IN_PLACE)


#===========CURENT STATUS=====================

    CURENT_STATUS= (
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Pending Review', 'Pending Review'),
        ('Completed', 'Completed'),
        ('Approved', 'Approved'),
             

    )
    status = models.CharField(max_length=100, choices= CURENT_STATUS) 


#===========Specific Site Contact=========================================

    Specific_Site_Contact= models.CharField(max_length=300)


    #===========DOCUMENT LOCATION=========================================

    Document_Location= models.CharField(max_length=300)

    #===========COMMENT=========================================

    Comment = models.TextField()



    #===========DUE DATE=====================

    Estimated_completion_date = models.DateField() 

 # ==============DISPLAYING TABLE INFO
    def __str__(self):
       return'Individual_Responsible:{}, building:{}, Program:{}, category:{}, status: {}, Type:{}, Ranking:{}, Program_in_Place:{}'.format(self.Individual_Responsible, self.building, self.Program, self.category, self.status, self.Type, self.Ranking, self.Program_in_Place )
