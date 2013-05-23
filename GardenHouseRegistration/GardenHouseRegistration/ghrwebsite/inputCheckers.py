#------------------------------------------------------------------------------#
#         Author: Jerald James A. Capao (jeraldjamescapao@gmail.com)
#                   University of Fribourg, Switzerland
#           E-Government Class Project - Garden House Registration
#                       Input Sanitizers / Checkers
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import re
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
def checkReqAcctForm(request, errors):

    if not request.POST.get('email_address', ''):
        errors.append('E-mail Address => cannot be empty.')
    else:
        errors = checkEmail(request.POST['email_address'], errors, 'E-mail Address') 

    if not request.POST.get('family_name', ''):
        errors.append('Family Name => cannot be empty.')
    else:
        errors = checkName(request.POST['family_name'], errors, 'Family Name')

    if not request.POST.get('first_name', ''):
        errors.append('First Name => cannot be empty.')
    else:
        errors = checkName(request.POST['first_name'], errors, 'First Name')

    if not request.POST.get('address_street', ''):
        errors.append('Street Address => cannot be empty.')
    else:
        errors = checkStreetAddress(request.POST['address_street'], errors, 'Street Address')

    if not request.POST.get('address_number', ''):
        errors.append('House/Apt. Number => cannot be empty.')
    else:
        errors = checkNumberAddress(request.POST['address_number'], errors, 'House Number')

    if not request.POST.get('address_postcode', ''):
        errors.append('Postal Code => cannot be empty.')
    else:
        errors = checkPostCodeAddress(request.POST['address_postcode'], errors, 'Postal Code')

    if not request.POST.get('mobile_number', ''):
        errors.append('Mobile Number => cannot be empty.')
    else:
        errors = checkContactNumber(request.POST['mobile_number'], errors, 'Mobile No.')

    # This field is not mandatory
    if request.POST.get('landline_number', ''):
        errors = checkContactNumber(request.POST['landline_number'], errors, 'Landline No.')

    return errors

#------------------------------------------------------------------------------#
def checkEditMunProf(request, errors):

    passwordFlag = True

    if not request.POST.get('password1', ''):
        errors.append('Password1 => cannot be empty.')
        passwordFlag = False
    else:
        errors = checkPassword(request.POST['password1'], errors, 'Password1')

    if not request.POST.get('password1_confirm', ''):
        errors.append('Confirm Password1 => cannot be empty.')
    else:
        errors = checkPassword(request.POST['password1_confirm'], errors, 'C. Password1')
        errors = checkPasswordEquivalence(request.POST['password1'], request.POST['password1_confirm'], errors)

    if not request.POST.get('password2', ''):
        errors.append('Password2 => cannot be empty.')
        passwordFlag = False
    else:
        errors = checkPassword(request.POST['password2'], errors, 'Password2')

    if not request.POST.get('password2_confirm', ''):
        errors.append('Confirm Password2 => cannot be empty.')
    else:
        errors = checkPassword(request.POST['password2_confirm'], errors, 'C. Password2')
        errors = checkPasswordEquivalence(request.POST['password2'], request.POST['password2_confirm'], errors)

    # Password1 and Password2 must not be equal
    if passwordFlag:
        if request.POST['password1'] == request.POST['password2']:
            errors.append('Password1 and Password2 cannot be the same value.')

    if not request.POST.get('address_street', ''):
        errors.append('Street Address => cannot be empty.')
    else:
        errors = checkStreetAddress(request.POST['address_street'], errors, 'Street Address')

    if not request.POST.get('address_number', ''):
        errors.append('House/Bldg. Number => cannot be empty.')
    else:
        errors = checkNumberAddress(request.POST['address_number'], errors, 'Bldg. Number')

    if not request.POST.get('address_postcode', ''):
        errors.append('Postal Code => cannot be empty.')
    else:
        errors = checkPostCodeAddress(request.POST['address_postcode'], errors, 'Postal Code')

    # These fields are not mandatory
    if request.POST.get('phone_number', ''):
        errors = checkContactNumber(request.POST['phone_number'], errors, 'Phone No.')

    if request.POST.get('fax_number', ''):
        errors = checkContactNumber(request.POST['fax_number'], errors, 'Phone No.')

    if request.POST.get('landline_number', ''):
        errors = checkContactNumber(request.POST['landline_number'], errors, 'Landline No.')

    return errors

#------------------------------------------------------------------------------#
def checkLoginForm(request, errors):

    if not request.POST.get('email_address', ''):
        errors.append('E-mail Address => cannot be empty.')
    else:
        errors = checkEmail(request.POST['email_address'], errors, 'E-mail Address') 

    if not request.POST.get('password', ''):
        errors.append('Password => cannot be empty.')
    else:
        errors = checkPassword(request.POST['password'], errors, 'Password')

    if not request.POST.get('confirm_password', ''):
        errors.append('Comfirm Password => cannot be empty.')
    else:
        errors = checkPassword(request.POST['confirm_password'], errors, 'C. Password')
        errors = checkPasswordEquivalence(request.POST['password'], request.POST['confirm_password'], errors)

    return errors

#------------------------------------------------------------------------------#
def checkGHRequestForm(request, errors):

    if not request.POST.get('days_since_used', ''):
        errors.append('Days Since Used => cannot be empty.')
    else:
        errors = checkDaysSinceUsed(request.POST['days_since_used'], errors, 'Days Since Used')

    return errors

#------------------------------------------------------------------------------#
def CheckValidFileUploadType(content_type):

    if content_type != 'image/jpeg' or content_type != 'application/pdf' or content_type != 'application/gif' or content_type != 'application/png':
        return False
    else:
        return True

#-------------------------------------------------------------------------#
def checkDaysSinceUsed(days_since_used, errors, caption):

    errors = checkIllegalCharacters(days_since_used, errors, caption, '-()![]@_&%\"\\=?;^*:~`#|${}<>abcdefghijklmnopqrstuvwxyz')

    if int(days_since_used) > 90:
        errors.append('Days Since Used => Are you sure that it has been more than 90 days since used? You will be fined according to the legislation if that\is the case.')

    return errors

#------------------------------------------------------------------------------#
def checkEmail(email_address, errors, caption):

    try:
        validate_email(email_address)
    except ValidationError:
        errors.append(caption + ' => please enter a valid one')

    return errors

#------------------------------------------------------------------------------#
def checkName(name, errors, caption):

    errors = checkIllegalCharacters(name, errors, caption, '![]()@_&%+\"\\=?;^*:~`#|${}<>0123456789')

    if len(name) > 15:
        errors.append(caption + ' => must not be more than 15 characters.')

    return errors

#------------------------------------------------------------------------------#
def checkStreetAddress(streetAddress, errors, caption):

    errors = checkIllegalCharacters(streetAddress, errors, caption, '![]@_&%+\"\\=?;^*:~`#|${}<>')

    if len(streetAddress) > 50:
        errors.append(caption + ' => must not be more than 50 characters.')
    if len(streetAddress) < 5:
        errors.append(caption + ' => too short; less than 5 characters.')

    return errors

#------------------------------------------------------------------------------#
def checkNumberAddress(numberAddress, errors, caption):

    errors = checkIllegalCharacters(numberAddress, errors, caption, '!()[]@_&%+\"\\=?;^*:~`#|${}<>')

    if len(numberAddress) > 8:
        errors.append(caption + ' => must not be more than 8 characters.')

    if not re.match('[0-9]+', numberAddress):
        errors.append('House No. => must be composed of numbers only.')

    return errors

#------------------------------------------------------------------------------#
def checkPostCodeAddress(postCodeAddress, errors, caption):

    errors = checkIllegalCharacters(postCodeAddress, errors, caption, '!()[]@_&%+\"\\=?;^*:~`#|${}<>abcdefghijklmnopqrstuvwxyz')

    if len(postCodeAddress) > 4 or len(postCodeAddress) < 4:
        errors.append(caption + ' => must be exactly 4 characters.')

    if not re.match('[0-9]+', postCodeAddress):
        errors.append('Postal Code => must be composed of numbers only.')

    return errors

#------------------------------------------------------------------------------#
def checkContactNumber(contactNumber, errors, caption):

    errors = checkIllegalCharacters(contactNumber, errors, caption, '![]@_&%\"\\=?;^*:~`#|${}<>abcdefghijklmnopqrstuvwxyz')

    if len(contactNumber) > 15:
        errors.append(caption + ' => must not be more than 20 characters.')

    if not re.match('[0-9()-]+', contactNumber):
        errors.append(caption + ' => must be composed of numbers only.')

    return errors

#------------------------------------------------------------------------------#
def checkPassword(password, errors, caption):

    errors = checkIllegalCharacters(password, errors, caption, ' @_!()[]&%+\"\\=?;^*:~`#|${}<>')

    if len(password) > 12:
        errors.append(caption + ' => must not be more than 12 characters.')

    if len(password) < 6:
        errors.append(caption + ' => must not be less than 6 characters.')

    return errors

#------------------------------------------------------------------------------#
def checkPasswordEquivalence(password, confirm_password, errors):

    if password != confirm_password:
        errors.append('Passwords => must match.')

    return errors

#------------------------------------------------------------------------------#
def checkIllegalCharacters(string, errors, caption, illegalCharacterSeries):

    illegalcharacters = illegalCharacterSeries

    illegalCharCount = 0
    for i in string:
        if i in illegalcharacters:
            errors.append(caption + ' => Illegal character/s detected: \'' + i + '\'')
            illegalCharCount = illegalCharCount + 1
            break

    return errors

#------------------------------------------------------------------------------#