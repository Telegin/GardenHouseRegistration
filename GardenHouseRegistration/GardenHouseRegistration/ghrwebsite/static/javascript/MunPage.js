/**************************************************************************
 *      Author: Jerald James A. Capao (jeraldjamescapao@gmail.com)
 *              University of Fribourg, Switzerland
 *       E-Government Class Project - Garden House Registration
 *                Javascript for Municipal Page
 **************************************************************************/

function confirmAcceptAcctReq() {
    
    if (confirm('Are you sure that you want to ACCEPT this account request?')) {
        return true;
    } else {
        return false;
    }
}

function confirmDenyAcctReq() {

    if (confirm('Are you sure that you want to DENY this account request?')) {
        return true;
    } else {
        return false;
    }
}

function confirmPrint() {

    if (confirm('Print the user\'s confirmation letter?')) {
        return true;
    } else {
        return false;
    }

}

function confirmAcceptGHR() {

    if (confirm('Are you sure that you want to ACCEPT this Garden House Registration request?')) {
        return true;
    } else {
        return false;
    }

}

function confirmDenyGHR() {

    if (confirm('Are you sure that you want to DENY this Garden House Registration request?')) {
        return true;
    } else {
        return false;
    }

}