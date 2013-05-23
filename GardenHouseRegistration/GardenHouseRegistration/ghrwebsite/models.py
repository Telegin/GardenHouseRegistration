#------------------------------------------------------------------------------#
#         Author: Jerald James A. Capao (jeraldjamescapao@gmail.com)
#                   University of Fribourg, Switzerland
#           E-Government Class Project - Garden House Registration
#                         Base System Essentials
from django.db import models
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------# 
class Canton(models.Model):

    canton_id      = models.AutoField(primary_key = True)
    canton_initial = models.CharField(max_length = 2)
    canton_name    = models.CharField(max_length = 30)

#------------------------------------------------------------------------------# 
class Municipality(models.Model):

    municipality_id    = models.AutoField(primary_key = True)

    email_address      = models.EmailField()              # Used for Login
    password1          = models.CharField(max_length = 12)
    password2          = models.CharField(max_length = 12)
    municipality_name  = models.CharField(max_length = 35)
    address_street     = models.CharField(max_length = 50, blank = True)
    address_number     = models.SmallIntegerField(blank = True)   # Office Place No.
    address_postcode   = models.SmallIntegerField(blank = True)   # Postal Code
    postal_case_no     = models.SmallIntegerField(blank = True)
    phone_number       = models.IntegerField(blank = True)
    fax_number         = models.IntegerField(blank = True)
    opening_hours      = models.TextField()
    canton             = models.ForeignKey(Canton)

#------------------------------------------------------------------------------#
class User(models.Model):

    user_id          = models.AutoField(primary_key = True)
    address_commune  = models.ForeignKey(Municipality)

    email_address    = models.EmailField()              # Used for Login
    password1        = models.CharField(max_length = 12)
    password2        = models.CharField(max_length = 12)
    family_name      = models.CharField(max_length = 15)
    first_name       = models.CharField(max_length = 15)
    address_street   = models.CharField(max_length = 50)
    address_number   = models.CharField(max_length = 8)     # House/Apt. No.
    address_postcode = models.CharField(max_length = 4)     # Postal Code
    mobile_number    = models.CharField(max_length = 15)
    landline_number  = models.CharField(max_length = 15, blank = True)

    # 0 = Requested, 1 = Accepted
    account_request_status = models.SmallIntegerField()

    # Important dates to be displayed
    # <date_granted> will be initially null on the database
    # The value of <date_granted> won't be empty if reg. is accepted
    date_requested   = models.DateTimeField()
    date_updated     = models.DateTimeField()
    date_granted     = models.DateTimeField(null = True)

    # Returns a unicode object as a model string representation
    # Format: <family_name >, <first_name>
    def __unicode__(self):
        return u'%s, %s' % (self.family_name, self.first_name)

    # For ordering in the Municipality Page => Account Requests Section
    # Asc order => The communal staff must see the oldest requests first
    class Meta:
        ordering = ['date_requested', 'family_name', 'first_name']

#------------------------------------------------------------------------------# 
class RequirementsForRegistration(models.Model):

    what_commune = models.ForeignKey(Municipality)
    requirements = models.TextField()

#------------------------------------------------------------------------------# 
class GardenHouseReg(models.Model):
    
    registration_id  = models.AutoField(primary_key = True)
    who_registered   = models.ForeignKey(User)
    belongs_to       = models.ForeignKey(Municipality)
    days_since_used  = models.SmallIntegerField()
    date_updated     = models.DateTimeField()
    date_granted     = models.DateTimeField(null = True)

    # 0 = Requested, 1 = Accepted, 2 = Denied
    status = models.SmallIntegerField()

#------------------------------------------------------------------------------# 
class UploadedFiles(models.Model):

    # What garden house registration is this uploaded file belongs?
    what_gh_registration = models.ForeignKey(GardenHouseReg)
    file_name            = models.CharField(max_length = 100)
    date_uploaded        = models.DateTimeField()

#------------------------------------------------------------------------------# 