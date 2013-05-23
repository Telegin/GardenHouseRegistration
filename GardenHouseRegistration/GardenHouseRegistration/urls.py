#-------------------------------------------------------------------------#
#     Author: Jerald James A. Capao (jeraldjamescapao@gmail.com)
#             University of Fribourg, Switzerland
from django.conf.urls import patterns, include, url
from GardenHouseRegistration.ghrwebsite import views
#-------------------------------------------------------------------------#

#-------------------------------------------------------------------------#
urlpatterns = patterns('',

    (r'^$', views.Homepage),            
    (r'^LegalSpecEng/$', views.LegalSpecEng),   # English version
    (r'^LegalSpecFr/$', views.LegalSpecFr),     # French version
    (r'^ReqAcct/$', views.ReqAcct),             # Request for an Account
    (r'^ReqAcct/ReqAcctSuccess.html$', views.ReqAcctSuccess),  
    (r'^WhatCanton/$', views.WhatCanton),
    (r'^NoRegisteredMunicipalities.html/$', views.NoRegisteredMunicipalities),
    (r'^Login/$', views.Login),
    (r'^Logout/$', views.Logout),
    (r'^MunPage/$', views.MunPage),
    (r'^UserPage/$', views.UserPage),
    (r'^ManageAcctRequest/$', views.ManageAcctRequest),
    (r'^PrintConfirmation/$', views.PrintConfirmation),
    (r'^ManageGHRRequest/$', views.ManageGHRRequest),
    (r'^EditMunProf/$', views.EditMunProf),
    (r'^RegisterGardenHouse/$', views.RegisterGardenHouse),
)
#-------------------------------------------------------------------------#
