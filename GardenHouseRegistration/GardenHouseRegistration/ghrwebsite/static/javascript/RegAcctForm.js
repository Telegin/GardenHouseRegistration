/**************************************************************************
 *      Author: Jerald James A. Capao (jeraldjamescapao@gmail.com)
 *              University of Fribourg, Switzerland
 *       E-Government Class Project - Garden House Registration
 *              Javascript for Request Account Form
 **************************************************************************/

function clearRegUserFields() {
    document.getElementById('email_address').value = '';
    document.getElementById('family_name').value = '';
    document.getElementById('first_name').value = '';
    document.getElementById('address_street').value = '';
    document.getElementById('address_number').value = '';
    document.getElementById('address_postcode').value = '';
    document.getElementById('mobile_number').value = '';
    document.getElementById('landline_number').value = '';
}

function confirmAcctReq() {
    var fName = document.forms['req_acct_form']['first_name'].value;
    if (confirm('Are you sure ' + fName + ' that you want to submit this account request?')) {
        return true;
    } else {
        return false;
    }
}
