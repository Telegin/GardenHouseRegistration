#-------------------------------------------------------------------------#
#      Author: Jerald James A. Capao (jeraldjamescapao@gmail.com)
#              University of Fribourg, Switzerland
#        E-Government Class Project - Garden House Registration
from GardenHouseRegistration.ghrwebsite.models import *
from django.contrib import sessions
from datetime import *
#-------------------------------------------------------------------------#

#-------------------------------------------------------------------------#
def UserExists(request):

    # We need to check if this user already exists in the database
    # Both User and Municipality accounts must be unique!
    # In this case we will use the email
    email = request.POST['email_address']

    if User.objects.filter(email_address = email).exists() or Municipality.objects.filter(email_address = email).exists():
        return True
    
    return False

#-------------------------------------------------------------------------#
def GetMunicipalityList(chosen_canton_id):

    return Municipality.objects.filter(canton_id = chosen_canton_id).order_by('municipality_name')

#-------------------------------------------------------------------------#
def InsertRequestAccount(request, generated_passwords):

    # Creating a Municipality instance for address_commune
    municipalities = Municipality.objects.filter(municipality_id = request.POST['select_municipality'])

    u = User(   address_commune  = municipalities[0],
                email_address    = request.POST['email_address'],
                password1        = generated_passwords[0],
                password2        = generated_passwords[1],
                family_name      = request.POST['family_name'],
                first_name       = request.POST['first_name'],
                address_street   = request.POST['address_street'],
                address_number   = request.POST['address_number'],
                address_postcode = request.POST['address_postcode'],
                mobile_number    = request.POST['mobile_number'],
                landline_number  = request.POST['landline_number'],
                account_request_status = 0,
                date_requested   = datetime.now(),
                date_updated     = datetime.now(),
                date_granted     = None
            )

    u.save()

#-------------------------------------------------------------------------#
def InsertGHRRequest(request, id):
    
        user = GetUserDetails(id)
        municipality = GetMunicipality(user.address_commune_id)

        ghrr = GardenHouseReg(  who_registered   = user,
                                belongs_to       = municipality,
                                days_since_used  = request.POST['days_since_used'],
                                date_updated     = datetime.now(),
                                date_granted     = None,
                                status           = 0
                             )
        ghrr.save()
        return ghrr
    

#-------------------------------------------------------------------------#
def InsertUploadedFileData(ghrr, file_name):

    ufd = UploadedFiles (
                what_gh_registration = ghrr,
                file_name            = file_name,
                date_uploaded        = datetime.now()
          )
    ufd.save()

#-------------------------------------------------------------------------#
def UserPasswordIsCorrect(request):

    email = request.POST['email_address']
    password = request.POST['password']

    if User.objects.filter(email_address = email, password1 = password).exists() or Municipality.objects.filter(email_address = email, password1 = password).exists():
        return True
    
    if User.objects.filter(email_address = email, password2 = password).exists() or Municipality.objects.filter(email_address = email, password2 = password).exists():
        return True
    
    return False

#-------------------------------------------------------------------------#
def WhichKindOfUser(request):

    email = request.POST['email_address']
    kind = 'user'

    if Municipality.objects.filter(email_address = email).exists():
        kind = 'municipality'
        
    return kind

#-------------------------------------------------------------------------#  
def GetUserID(request, kind):

    email = request.POST['email_address']
    id = 0

    if kind == 'municipality':
        m = Municipality.objects.get(email_address = email)
        if m:
            id = m.municipality_id
    else:
        u = User.objects.get(email_address = email)
        if u:
            id = u.user_id

    return id
#-------------------------------------------------------------------------#   
def GetUsersWhoRequestedForAnAcct():

    return User.objects.filter(account_request_status = 0).order_by('date_requested')

#-------------------------------------------------------------------------#  
def AcceptAcctRequest(request):

    u = User.objects.get(user_id = request.POST['UserID'])

    if u:
        u.account_request_status = 1
        u.date_granted = datetime.now()
        u.save()

#-------------------------------------------------------------------------#  
def DenyAcctRequest(request):

    u = User.objects.get(user_id = request.POST['UserID'])

    if u:
        u.delete()

#-------------------------------------------------------------------------#  
def GetUsersWhoAreAlreadyAccepted():

    return User.objects.filter(account_request_status = 1).order_by('-date_granted')

#-------------------------------------------------------------------------#  
def GetUserDetails(userID):

    return User.objects.get(user_id = userID)

#-------------------------------------------------------------------------#  
def GetMunicipality(address_commune):

    return Municipality.objects.get(municipality_id = address_commune)

#-------------------------------------------------------------------------#  
def GetCantonInitial(address_commune):

    cantonInitial = ''
    m = Municipality.objects.get(municipality_id = address_commune)

    if m:
        c = Canton.objects.get(canton_id = m.canton_id)
        if c:
            cantonInitial = c.canton_initial

    return cantonInitial

#-------------------------------------------------------------------------#  
def GetGHRRequests():

    return GardenHouseReg.objects.filter(status = 0).order_by('date_updated')

#-------------------------------------------------------------------------#  
def AcceptGHRRequest(request):

    g = GardenHouseReg.objects.get(registration_id = request.POST['registration_id'])

    if g:
        g.status = 1
        g.date_granted = datetime.now()
        g.save()

#-------------------------------------------------------------------------#  
def DenyGHRRequest(request):

    g = GardenHouseReg.objects.get(registration_id = request.POST['registration_id'])

    if g:
        g.status = 2
        g.save()

#-------------------------------------------------------------------------#  
def GetGHRWhichAreAlreadyAccepted():

    return GardenHouseReg.objects.filter(status = 1).order_by('-date_granted')

#-------------------------------------------------------------------------#  
def GetMunicipalityDetails(id):

    return Municipality.objects.get(municipality_id = id)

#-------------------------------------------------------------------------#  
def UpdateMunProf(request):

    m = Municipality.objects.get(municipality_id = request.session['loggedin'])

    m.password1 = request.POST['password1']
    m.password2 = request.POST['password2']
    m.address_street = request.POST['address_street']
    m.address_number = request.POST['address_number']
    m.address_postcode = request.POST['address_postcode']
    m.phone_number = request.POST['phone_number']
    m.fax_number = request.POST['fax_number']
    m.opening_hours = request.POST['opening_hours']

    m.save()

#-------------------------------------------------------------------------#  
def GetGardenHouseReg(id):

    return GardenHouseReg.objects.filter(who_registered = id)

#-------------------------------------------------------------------------# 
def GetAttachments(registration_id):

    return UploadedFiles.objects.filter(what_gh_registration = registration_id)

#-------------------------------------------------------------------------# 