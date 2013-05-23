#-------------------------------------------------------------------------#
#      Author: Jerald James A. Capao (jeraldjamescapao@gmail.com)
#              University of Fribourg, Switzerland
#        E-Government Class Project - Garden House Registration
#-------------------------------------------------------------------------#

#-------------------------------------------------------------------------#
def EmailAlreadyExists():

    message = 'The E-mail address provided already exists on the DB. '
    message += 'If this e-mail is yours, why don\'t you login instead?'

    return message

#-------------------------------------------------------------------------#
def UserDoesNotExists():

    message = 'The E-mail address provided doesn\'t exists on the DB. '
    message += 'All accounts must be approved by the municipality before usage.'

    return message
#-------------------------------------------------------------------------#
def PasswordNotCorrect():

    message = 'The password provided doesn\'t match on the DB. '
    message += 'Please check your inputs'

    return message

#-------------------------------------------------------------------------#
def AcctReqPending():

    message = 'Account Registration Request still pending.'

    return message

#-------------------------------------------------------------------------#
def AcctReqDenied():

    message = 'Sorry, Acct. Registration Request denied. '
    message += 'Please contact your municipality.'

    return message

#-------------------------------------------------------------------------#