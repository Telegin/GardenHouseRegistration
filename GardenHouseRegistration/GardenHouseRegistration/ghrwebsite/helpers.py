#-------------------------------------------------------------------------#
#      Author: Jerald James A. Capao (jeraldjamescapao@gmail.com)
#              University of Fribourg, Switzerland
#        E-Government Class Project - Garden House Registration
from GardenHouseRegistration.ghrwebsite.models import *
import random
import os
#-------------------------------------------------------------------------#

#-------------------------------------------------------------------------#
def GenerateRandomPasswords():

    allowedCharacters  = '0123456789abcdefghijklmnopqrstuvwxyz'
    generatedPassword  = ''
    generatedPasswords = []

    i = 0
    while i < 2:
        # The generated random password will consist of 10 characters
        j = 0
        while j < 10:
            generatedPassword += random.choice(allowedCharacters)
            j = j + 1
        # Before we append the generated password, we must ensure that there is no
        # the same password on the database! :)
        if not (User.objects.filter(password1 = generatedPassword).exists() or User.objects.filter(password2 = generatedPassword).exists()):
            generatedPasswords.append(generatedPassword)
            generatedPassword = ''    # Resets the generated password object
            i = i + 1

    return generatedPasswords

#-------------------------------------------------------------------------#
def GetPathToMedia():

    return os.path.join(os.path.realpath(os.path.dirname(__file__))) + '/static/uploads/' 

#-------------------------------------------------------------------------#