from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from django import forms
# Create your models here.
# Start Notification Here
#/////////////////////////////////////////////////////
from django.db.models import signals
# from notification import models as notification



class SustainableReport(models.Model):

    class Meta:
        verbose_name = 'Sustainability Report'
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
    Type = models.CharField(max_length=20, choices=TYPES)


#======== CATEGORY==========================


    CATEGORY_STATEMENTS= (
         ('Monthly Statement', 'Monthly Statement'),
         ('Quarterly Statement', 'Quarterly Statement'),
         ('Annual Statement','Annual Statement'),
         
     )
    category = models.CharField(max_length=150, choices=CATEGORY_STATEMENTS)

#======Consumped===========================
    Amount_Consumed = models.CharField(max_length=15)
    Amount_Spent = models.CharField(max_length=15)

#===========UNIT TYPE=====================
    UNITS= (
        ('kWh', 'kWh'),
        ('Therms', 'Therms'),
        ('Gallons', 'Gallons'),
       
    )
    unit = models.CharField(max_length=16, choices=UNITS)


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
       return'data_Recorded_By:{},building:{}, city:{}, region: {}, Type :{}, Amount_Consumed:{}, unit:{}, Amount_Spent:{}'.format(self.data_Recorded_By, self.building, self.city, self.region, self.Type, self.Amount_Consumed,self.unit, self.Amount_Spent)

#==========NOTIFICATION STATUS REPORT=================================

def create_notice_types(app, created_models, verbosity, **kwargs):
    notification.create_notice_type("new_comment", "Comment posted", "A comment has been posted")
    signals.post_syncdb.connect(create_notice_types, sender=notification)

def new_comment(sender, instance, created, **kwargs):
    # remove this if-block if you want notifications for comment edit too
    if not created:
        return None

    context = {
        'comment': instance,
        'site': Site.objects.get_current(),
    }
    recipients = []

    # add all users who commented the same object to recipients
    for comment in instance.__class__.objects.for_model(instance.content_object):
        if comment.user not in recipients and comment.user != instance.user:
            recipients.append(comment.user)

    # if the commented object is a user then notify him as well
    if isinstance(instance.content_object, models.get_model('auth', 'User')):
        # if he his the one who posts the comment then don't add him to recipients
        if instance.content_object != instance.user and instance.content_object not in recipients:
            recipients.append(instance.content_object)

    notification.send(recipients, 'new_comment', context)

    signals.post_save.connect(new_comment, sender=models.get_model('comments', 'Comment'))

#==========NOTIFICATION END HERE================================================================
