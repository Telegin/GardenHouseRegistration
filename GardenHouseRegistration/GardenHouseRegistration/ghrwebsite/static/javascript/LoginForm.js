/**************************************************************************
 *      Author: Jerald James A. Capao (jeraldjamescapao@gmail.com)
 *              University of Fribourg, Switzerland
 *       E-Government Class Project - Garden House Registration
 *                Javascript for the Login Form
 **************************************************************************/

function clearLoginFields() {

    document.getElementById('email_address').value = '';
    document.getElementById('password').value = '';
    document.getElementById('comfirm_password').value = '';

}

function confirmLogin() {

    if (confirm('Do you wish to proceed to login?')) {
        return true;
    } else {
        return false;
    }
}
