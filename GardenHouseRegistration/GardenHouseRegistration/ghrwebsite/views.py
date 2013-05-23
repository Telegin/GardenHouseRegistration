#-------------------------------------------------------------------------#
#      Author: Jerald James A. Capao (jeraldjamescapao@gmail.com)
#              University of Fribourg, Switzerland
#        E-Government Class Project - Garden House Registration
from datetime import *
import os
from django.shortcuts import render_to_response
from django.template import Context
from django.template import RequestContext
from django.contrib import sessions
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from GardenHouseRegistration.ghrwebsite import inputCheckers
from GardenHouseRegistration.ghrwebsite.models import *
from GardenHouseRegistration.ghrwebsite import dbTouchers
from GardenHouseRegistration.ghrwebsite import helpers
from GardenHouseRegistration.ghrwebsite import messages
#-------------------------------------------------------------------------#

#-------------------------------------------------------------------------#
def Homepage(request):

    # Will expire when the Web browser of the user is closed
    request.session.set_expiry(0)  

    # Loading the homepage template
    return render_to_response('Homepage.html', context_instance = RequestContext(request))

#-------------------------------------------------------------------------#
def LegalSpecEng(request):

    # Loading the legal specification (English Version) page template
    return render_to_response('LegalSpecEng.html', context_instance = RequestContext(request))

#-------------------------------------------------------------------------#
def LegalSpecFr(request):

    # Loading the legal specification (English Version) page template
    return render_to_response('LegalSpecFr.html', context_instance = RequestContext(request))

#-------------------------------------------------------------------------#
# THE FIRST CONCERN IS HERE
# THE FIRST CONCERN IS HERE
# THE FIRST CONCERN IS HERE
# THE FIRST CONCERN IS HERE
# THE FIRST CONCERN IS HERE
#-------------------------------------------------------------------------#
@csrf_exempt 
def ReqAcct(request):
    
    inputCheckErrors = []
    # The source of request is 'ReqAcctForm.html'
    if request.method == 'POST':
        inputCheckErrors = inputCheckers.checkReqAcctForm(request, inputCheckErrors)
        # We need to check if this user already exists in the database
        if dbTouchers.UserExists(request):
            inputCheckErrors.append(messages.EmailAlreadyExists)
        if not inputCheckErrors:
            # Generate 2 Random passwords
            generatedPasswords = helpers.GenerateRandomPasswords()
            # Insert the user account request to the database
            dbTouchers.InsertRequestAccount(request, generatedPasswords)
            del request.session['chosenCanton']
            # THEN IN THIS AREA THE USER MUST RECEIVE AN EMAIL FOR AUTHENTICATION
            # THEN IN THIS AREA THE USER MUST RECEIVE AN EMAIL FOR AUTHENTICATION
            # THEN IN THIS AREA THE USER MUST RECEIVE AN EMAIL FOR AUTHENTICATION
            # THEN IN THIS AREA THE USER MUST RECEIVE AN EMAIL FOR AUTHENTICATION
            # THEN IN THIS AREA THE USER MUST RECEIVE AN EMAIL FOR AUTHENTICATION
            return HttpResponseRedirect('ReqAcctSuccess.html')

    # The source of request is 'WhatCanton.html'
    if request.method == 'GET':
        # Stores temporarily the chosen canton id into the session
        request.session['chosenCanton'] = request.GET['select_canton']

    try:
        # Used for populating the registered municipalities dropdown listbox
        municipalityList = dbTouchers.GetMunicipalityList(request.session['chosenCanton'])
        municipalityList[0]   # Checking if the query result is empty
    except IndexError:
        return render_to_response('NoRegisteredMunicipalities.html')

    return render_to_response('ReqAcctForm.html',
        {
            'input_check_errors': inputCheckErrors,     
            'email_address'     : request.POST.get('email_address', ''),    
            'family_name'       : request.POST.get('family_name', ''),  
            'first_name'        : request.POST.get('first_name', ''),  
            'address_street'    : request.POST.get('address_street', ''),  
            'address_number'    : request.POST.get('address_number', ''),  
            'address_postcode'  : request.POST.get('address_postcode', ''),  
            'mobile_number'     : request.POST.get('mobile_number', ''),  
            'landline_number'   : request.POST.get('landline_number', ''),  
            'municipality_list' : municipalityList,
        },
    )

#-------------------------------------------------------------------------#
def ReqAcctSuccess(request):

    # Loading the Success Page of requesting an account
    return render_to_response('ReqAcctSuccess.html')

#-------------------------------------------------------------------------#
@csrf_exempt 
def EditMunProf(request):

    
        if request.session['loggedin'] and (request.session['pageURL'] == '/MunPage/'):

            inputCheckErrors = []
            # The source of request is 'EditMunProf.html'
            if request.method == 'POST':
                # Checking the user inputs
                inputCheckErrors = inputCheckers.checkEditMunProf(request, inputCheckErrors)
                if not inputCheckErrors:
                    dbTouchers.UpdateMunProf(request)
                    return HttpResponseRedirect('/MunPage/')
                else:
                    # Obtaining the Municipality Details
                    municipalityDetails = dbTouchers.GetMunicipalityDetails(request.session['loggedin'])       # Obtaining the Canton Initial
                    cantonInitial = dbTouchers.GetCantonInitial(municipalityDetails.canton_id)
                    return render_to_response('EditMunProf.html', 
                        {
                            'input_check_errors': inputCheckErrors,  
                            'email_address'     : municipalityDetails.email_address,            
                            'password1'         : request.POST.get('password1',''),      
                            'password2'         : request.POST.get('password2',''), 
                            'municipality_name' : municipalityDetails.municipality_name,
                            'address_street'    : request.POST.get('address_street',''), 
                            'address_number'    : request.POST.get('address_number',''), 
                            'address_postcode'  : request.POST.get('address_postcode',''), 
                            'phone_number'      : request.POST.get('phone_number',''), 
                            'fax_number'        : request.POST.get('fax_number',''), 
                            'opening_hours'     : request.POST.get('opening_hours',''), 
                            'canton_initial'    : cantonInitial,
                        },                   
                        context_instance = RequestContext(request)
                     )

            # Obtaining the Municipality Details
            municipalityDetails = dbTouchers.GetMunicipalityDetails(request.session['loggedin'])
            # Obtaining the Canton Initial
            cantonInitial = dbTouchers.GetCantonInitial(municipalityDetails.canton_id)

            return render_to_response('EditMunProf.html', 
                   {
                        'input_check_errors': inputCheckErrors,  
                        'email_address'     :  municipalityDetails.email_address,            
                        'password1'         : municipalityDetails.password1,      
                        'password2'         :     municipalityDetails.password2,
                        'municipality_name' : municipalityDetails.municipality_name,
                        'address_street'    : municipalityDetails.address_street,
                        'address_number'    : municipalityDetails.address_number,
                        'address_postcode'  : municipalityDetails.address_postcode,
                        'phone_number'      :   municipalityDetails.phone_number,
                        'fax_number'        :      municipalityDetails.fax_number,
                        'opening_hours'     : municipalityDetails.opening_hours,
                        'canton_initial'    : cantonInitial,
                   },                   
                   context_instance = RequestContext(request)
            )
        else:
            return HttpResponseRedirect('/Login/')
    #except KeyError:
        return HttpResponseRedirect('/Login/')

#-------------------------------------------------------------------------#
def WhatCanton(request):

    # Obtaining all canton names from the database
    allCanton = Canton.objects.order_by('canton_name')

    # Loading the Question: "From what canton are you?" page
    return render_to_response('WhatCanton.html', 
        {
            'allCanton' : allCanton
        },
    )

#-------------------------------------------------------------------------#
def NoRegisteredMunicipalities(request):

    # Just displaying that there are no municipalities registered in a
    # particular canton
    return render_to_response('NoRegisteredMunicipalities.html')

#-------------------------------------------------------------------------#
@csrf_exempt 
def Login(request):

    inputCheckErrors = []
    # The source of request is 'LoginForm.html'
    if request.method == 'POST':
        inputCheckErrors = inputCheckers.checkLoginForm(request, inputCheckErrors)
        if not inputCheckErrors:
            # We need to check if this user doesn't exists in the database
            if not dbTouchers.UserExists(request):
                inputCheckErrors.append(messages.UserDoesNotExists)
            else:
                if not dbTouchers.UserPasswordIsCorrect(request):
                    inputCheckErrors.append(messages.PasswordNotCorrect)
            if not inputCheckErrors:
                # Check first what kind of User => Common or Municipality
                if dbTouchers.WhichKindOfUser(request) == 'municipality':
                    # Setting the session for this Municipality
                    request.session['loggedin'] = dbTouchers.GetUserID(request, 'municipality')
                    request.session['pageURL'] = '/MunPage/'
                    return HttpResponseRedirect('/MunPage/')
                else:
                    # Setting the session for this User
                    request.session['loggedin'] = dbTouchers.GetUserID(request, 'user')
                    request.session['pageURL'] = '/UserPage/'
                    return HttpResponseRedirect('/UserPage/')

    return render_to_response('Login.html',
        {
            'input_check_errors': inputCheckErrors,     
            'email_address'     : request.POST.get('email_address', ''),    
        }
    )

#-------------------------------------------------------------------------#
def Logout(request):

    try:
        if request.session['loggedin'] and request.session['pageURL']:
            del request.session['loggedin']
            del request.session['pageURL']
    except KeyError:
        return render_to_response('Homepage.html', context_instance = RequestContext(request))

    return render_to_response('Homepage.html')

#-------------------------------------------------------------------------#
def MunPage(request):

    try:
        if request.session['loggedin'] and (request.session['pageURL'] == '/MunPage/'):
            # Obtaining the list of users who requested for an Account
            usersWhoRequested = dbTouchers.GetUsersWhoRequestedForAnAcct()
            usersAlreadyAccepted = dbTouchers.GetUsersWhoAreAlreadyAccepted()
            allGHRrequests = dbTouchers.GetGHRRequests()
            GHRegistrants = []
            for ghrrequest in allGHRrequests:
                GHRegistrants.append(dbTouchers.GetUserDetails(ghrrequest.who_registered_id))
            zipped = zip(allGHRrequests, GHRegistrants)
            ghrAlreadyAccepted = dbTouchers.GetGHRWhichAreAlreadyAccepted()
            GHRegistrants2 = []
            for ghrrequest in ghrAlreadyAccepted:
                GHRegistrants2.append(dbTouchers.GetUserDetails(ghrrequest.who_registered_id))
            zipped2 = zip(ghrAlreadyAccepted, GHRegistrants2)
            return render_to_response('MunPage.html', 
                {
                    'users_who_requested' : usersWhoRequested,  
                    'users_who_are_accepted': usersAlreadyAccepted,
                    'ghr_registrants' : GHRegistrants,
                    'zipped' : zipped,
                    'zipped2' : zipped2,
                    'ghr_already_accepted' : ghrAlreadyAccepted, 
                },
                context_instance = RequestContext(request),
            )
        else:
            return HttpResponseRedirect('/Login/')
    except KeyError:
        return HttpResponseRedirect('/Login/')

#-------------------------------------------------------------------------#
def UserPage(request):

    try:
        if request.session['loggedin'] and (request.session['pageURL'] == '/UserPage/'):
            # Obtaining the list of Garden House Registrations of this user
            MyGHR = dbTouchers.GetGardenHouseReg(request.session['loggedin'])
            return render_to_response('UserPage.html', 
                {
                    'my_ghr' : MyGHR,
                },
                context_instance = RequestContext(request)
            )
        else:
            return HttpResponseRedirect('/Login/')
    except KeyError:
        return HttpResponseRedirect('/Login/')

#-------------------------------------------------------------------------#
@csrf_exempt 
def ManageAcctRequest(request): 

    # The source of request is 'MunPage.html'
    if request.method == 'POST':
        try:
            if request.POST['Accept']:
                dbTouchers.AcceptAcctRequest(request)
                # We can put our logic here to send SMS to the accepted account
        except:
            dbTouchers.DenyAcctRequest(request)

    return HttpResponseRedirect('/MunPage/')

#-------------------------------------------------------------------------#
@csrf_exempt 
def PrintConfirmation(request):

    # The source of request is 'MunPage.html'
    if request.method == 'POST':
        try:
            if request.POST['Print']:
                theUser = dbTouchers.GetUserDetails(request.POST['UserID'])
                municipality = dbTouchers.GetMunicipality(theUser.address_commune_id)
                cantonInitial = dbTouchers.GetCantonInitial(theUser.address_commune_id)
                dateNow = date.today()
                return render_to_response('PrintConfirmation.html', 
                    {
                        'the_user' : theUser,
                        'municipality' : municipality,
                        'canton_initial' : cantonInitial,
                        'date_now' : dateNow,
                    },
                    context_instance = RequestContext(request)
                )
        except:
           return HttpResponseRedirect('/MunPage/') 

    return HttpResponseRedirect('/MunPage/')

#-------------------------------------------------------------------------#
@csrf_exempt 
def ManageGHRRequest(request): 

    # The source of request is 'MunPage.html'
    if request.method == 'POST':
        try:
            if request.POST['Accept']:
                dbTouchers.AcceptGHRRequest(request)
        except:
            try:
                if request.POST['Deny']:
                    dbTouchers.DenyGHRRequest(request)
            except:
                nothing = ''
                try:
                    if request.POST['Attachments']:
                        user = dbTouchers.GetUserDetails(request.POST['user_id'])
                        # Obtain the attachments which are related to this GH Registration ID
                        attachments = dbTouchers.GetAttachments(request.POST['registration_id'])
                        attachmentURLS = []
                        for a in attachments:
                            attachmentURLS.append('uploads/' + str(a.what_gh_registration_id) + '/' + a.file_name)                 
                        zipped = zip(attachments, attachmentURLS)
                        return render_to_response('Attachments.html',
                            {
                                'attachments' : attachments,
                                'zipped'    : zipped,
                                'registration_id' : request.POST['registration_id'],
                                'user' : user,
                            },
                            context_instance = RequestContext(request)                 
                        )
                except:
                    return HttpResponseRedirect('/MunPage/')
                    
    return HttpResponseRedirect('/MunPage/')

#-------------------------------------------------------------------------#
@csrf_exempt 
def RegisterGardenHouse(request):

    try:
        if request.session['loggedin'] and (request.session['pageURL'] == '/UserPage/'):
            good = 'good!'
        else:
            return HttpResponseRedirect('/Login/')
    except KeyError:
        return HttpResponseRedirect('/Login/')

    # The source of request is 'UserPage.html'
    if request.method == 'POST':
        inputCheckErrors = []
        if not ('files' in request.FILES):
            inputCheckErrors.append('File Upload/s => You didn\'t upload any files. It\'s mandatory so that your application will be more informative and less prone to rejection.')
        else:
            inputCheckErrors = inputCheckers.checkGHRequestForm(request, inputCheckErrors)
            # Iterating all over the files
            for aFile in request.FILES.getlist('files'):

                if aFile.size > 2000000: # 2MB
                    inputCheckErrors.append('File Size limit exceeded 2MB => ' + str(aFile.size/1000000) + 'MB detected.')

                if inputCheckers.CheckValidFileUploadType(aFile.content_type):
                    inputCheckErrors.append('File Upload Type Invalid => Found: ' + aFile.content_type)
        
        if not inputCheckErrors:
            try:
                # Saving registration request to the database
                ghrr = dbTouchers.InsertGHRRequest(request, request.session['loggedin'])
                
                # Write all uploaded attachments into the media folder
                mediaURL  = helpers.GetPathToMedia()
                mediaURL2 = mediaURL + str(ghrr.registration_id)

                # Creates a folder if it doesn't exists => Registration ID number
                if not os.path.exists(mediaURL + str(ghrr.registration_id)):
                    os.mkdir(os.path.join(mediaURL, str(ghrr.registration_id)))
                # Iterating all over the files to save it
                for aFile in request.FILES.getlist('files'):
                    fd = open('%s/%s' % (mediaURL2, str('') + str(aFile)), 'wb')
                    for chunk in aFile.chunks():
                        fd.write(chunk)
                    fd.close()
                    # Saving the uploaded file data to the database
                    dbTouchers.InsertUploadedFileData(ghrr, aFile.name)
                    
            except:
                inputCheckErrors.append('Saving to the Database Failed. Try again later.')

        if inputCheckErrors:
            # Obtaining the list of Garden House Registrations of this user
            MyGHR = dbTouchers.GetGardenHouseReg(request.session['loggedin'])
            return render_to_response('UserPage.html',
                {
                    'input_check_errors' : inputCheckErrors,
                    'days_since_used' : request.POST.get('days_since_used', ''), 
                    'my_ghr' : MyGHR,
                },
                context_instance = RequestContext(request) 
            )
            
    return HttpResponseRedirect('/UserPage/') 

#-------------------------------------------------------------------------#