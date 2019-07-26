from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from django import forms

#===========Project_Information=============================

class ProjectInformation(models.Model):
    class Meta:
        verbose_name = 'Project Information Record'
        

    RESPONSIBLE_PARTY = (
        ('Stanley Njoku', 'Stanley Njoku'),
        ('Beverly Everhart', 'Beverly Everhart'),
        ('Lenka Barrettova', 'Lenka Barrettova'),
        ('Chris Bradshaw', 'Chris Bradshaw'),
        ('Connie Gordon', 'Connie Gordon'),
        ('Xonie Lloyd', 'Xonie Lloyd'),
        ('Jeffrey Hamilton', 'Jeffrey Hamilton'),
    )
    person_Responsible = models.CharField(max_length=150, choices= RESPONSIBLE_PARTY)
   
# Project Category Type Dropdown Selection
    
    PROJECT_CATEGORY =(
        ('Safety','Safety'),
        ('Environment','Environment'),
        ('Fee',' Fee',),
        ('Regulatory', 'Regulatory'),
        ('Report','Report')
    )
    category = models.CharField(max_length=150, choices = PROJECT_CATEGORY)

# Project Type Dropdown Selection
    PROJECT_TYPE = (
        ('Hazardous Waste Management', 'Hazardous Waste Management'),
        ('Confined Space', 'Confined Space'),
        ('Emergency Response Management', ' Emergency Response Management',),
        ('Storm Water', 'Storm Water'),
        ('Hazardous Management Business Plan', 'Hazardous Management Business Plan'),
        ('Respiratory Fit Testing', 'Respiratory Fit Testing'),
        ('Worker Compensation', 'Worker Compensation'),
        ('Ergonomics', 'Ergonomics'),
        ('Respiratory Fit Testing', 'Respiratory Fit Testing'),
        ('Job Hazard Analysis', 'Job Hazard Analysis'),
        ('Lockout/tagout Procedures', 'Lockout/tagout Procedures'),
        ('Machine Safety', 'Machine Safety'),
        ('Chemical Hazard Communication', 'Chemical Hazard Communication'),
        ('Accident Prevention Programs', 'Accident Prevention Programs'),

    )
    Type= models.CharField(max_length =150, choices=PROJECT_TYPE)

    # RADIO BUTTON

    PROJECT_STATUS = (
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Pending Review', 'Pending Review',),
        ('On Hold', 'On Hold'),
        ('Approved', 'Approved'),
    )
    status = models.CharField(max_length=150, choices=PROJECT_STATUS)

    #Add Additional Field Lines
    date_added = models.DateTimeField(default=datetime.now)
    estimated_completion = models.DateField()
    comment = models.TextField()

#============Modifying Table to Read information ======================
    def __str__(self):
       return'person_Responsible:{}, Category: {}, Type:{}, Status:{}'.format(self.person_Responsible, self.category, self.Type, self.status)

#=================Manifest Class==============================================


class Manifest(models.Model):
    Name= models.CharField(max_length=200)
    Manifest_Tracking_Number = models.CharField(max_length=200,)
    EPA_ID_Location = models.CharField(max_length=200)
    Building_Address = models.CharField(max_length=200)


    VENDOR_NAMES = (
        ('Clean Harbors', 'Clean Harbors'),
        ('Ingenium', 'Ingenium'),
        ('Veolia', 'Veolia'),
        
     )
    Vendor_Name = models.CharField(max_length=150, choices= VENDOR_NAMES)

    LOCATION_EPAID = (
         ('B2500 - CAL000342024', 'B2500 - CAL000342024'),
         ('B6000 - CAD983606872', 'B6000 - CAD983606872'),
         ('4000  - CAD981991276', '4000  - CAD981991276'),
         ('B2000 - CAD983606872', 'B2000 - CAD983606872'),
         ('B925  - CAR000158816', 'B925  - CAR000158816'),
         ('B3110 - CAD981453871', 'B3110 - CAD981453871'),
         ('B487 - CAL000248918', 'B487 - CAL000248918'),
         ('B5731 - CAL000346207', 'B5731 - CAL000346207'),
         ('B5500 - CAL000095938', 'B5500 - CAL000095938'),
         ('Select One', 'Select One'),
     )
    EPA_ID_Location = models.CharField(max_length=100, choices=LOCATION_EPAID, default='Select One')

    SHIPPING_TYPE = (
        ('Weekly Shipment', 'Weekly Shipment'),
        ('Monthly Shipment', 'Monthly Shipment'),
        ('90-day Shipment', '90-day Shipment',),
        ('180-day/270-day Shipment', '180-day/270-day Shipment'),
        ('Urgent Shipment', 'Urgent Shipment'),
        
    )
    Type= models.CharField(max_length =150, choices=SHIPPING_TYPE)


    CATEGORIES= (
         ('Drum Shipment', 'Drum Shipment'),
         ('Labpack', 'Labpack'),
         ('Bulk Shipment','Bulk Shipment'),
         
     )
    category = models.CharField(max_length=150, choices=CATEGORIES)

    Weight_Shipped = models.CharField(max_length=150)


    WEIGHT_UNITS= (
         ('Gallons (Liquid Only)', 'Gallons (Liquid Only)'),
         ('Kilograms', 'Kilograms'),
         ('Liters Liquid Only','Liters Liquid Only'),
         ('Metric Tons', 'Metric Tons'),
         ('Cubic Meter', 'Cubic Meter'),
         ('Pounds', 'Pounds'),
         ('Tons', 'Tons'),
         ('Cubic Yards', 'Cubic Yards'),
         ('Select One', 'Select One'),
     )
    weight_Unit = models.CharField(max_length=150, choices=WEIGHT_UNITS, default='Select One')
    
    def due_Date():
        return datetime.today() + timedelta(days=30)
    Date_Generator_Sgned = models.DateField(default=due_Date)
    
    Date_to_DTSC = models.DateField(default=due_Date)

    # def DateField():
     # date_added = DateField.DateField.strptime(start_Date,"%m/%d/%y")
     # estimated_completion = date_added+DateField.timedelta(days=30)

          
    MANIFEST_VENDOR = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    Manifest_Return_from_Vendor = models.CharField(max_length=150, choices=MANIFEST_VENDOR)

    MANIFEST_SIGNATURE = (
        ('Stanley Njoku', 'Stanley Njoku'),
        ('Beverly Everhart', 'Beverly Everhart'),
        ('Lenka Barrettova', 'Lenka Barrettova'),
        ('Chris Bradshaw', 'Chris Bradshaw'),
        ('Connie Gordon', 'Connie Gordon'),
        ('Kevin Tennyson', 'Kevin Tennyson'),
    )
    Manifest_Signatory = models.CharField(max_length=150, choices= MANIFEST_SIGNATURE)
    
    MANIFEST_FILING_STATUS = (
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Pending Review', 'Pending Review',),
        ('On Hold', 'On Hold'),
        ('Approved', 'Approved'),
    )
    status = models.CharField(max_length=150, choices=MANIFEST_FILING_STATUS)

    comment = models.TextField()


# ==========Read Manifest======================================================

    def __str__(self):
       return'Manifest_Tracking_Number:{}, EPA_ID_Location:{}, date_to_DTSC :{}, Manifest_Return_from_Vendor:{}'.format(self.Manifest_Tracking_Number, self.EPA_ID_Location, self.Date_to_DTSC, self.Manifest_Return_from_Vendor)


# ==========Read Manifest ENDS HERE=====================================================


#=================Compliance Class==============================================

class Compliance(models.Model):
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

    AGENCY_TYPE = (
        ('County', 'County'),
        ('Local', 'Local'),
        ('State', 'State',),
        ('Federal', 'Federal'),
        ('EPA', 'EPA'),
        ('OSHA', 'OSHA'),
    )
    Type = models.CharField(max_length=150, choices=AGENCY_TYPE)
    
    def due_Date():
       return datetime.today() + timedelta(days=30)

    start_Date = models.DateField(default=datetime.today)
    due_Date = models.DateField(default=due_Date)
    comment = models.TextField()

    COMPLIANCE_STATUS = (
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Pending Review', 'Pending Review',),
        ('On Hold', 'On Hold'),
        ('Approved', 'Approved'),
    )
    status = models.CharField(max_length=150, choices=COMPLIANCE_STATUS)

     
# Modifying Table to Read information ======================

    def __str__(self):
       return'Agency: {}, Description: {}, Type: {}, Start_Date:{}, Due_Date:{}'.format(self.agency, self.description, self.Type, self.start_Date, self.due_Date)


#=================Dashbaord==============================================

def index(request):
    return render(request,'management/index.html')
    num_compliance=Compliance.objects.all().count()
    num_manifest=Manifest.objects.all().count()

    return render(
        request,
        'management/index.html',
        context={'num_manifest':num_manifest,'num_compliance':num_compliance},  

      )

    #=================EPAS===============================================================
