from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from version1.api import *
from tastypie.api import Api
from django.contrib import admin

admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(CashWithdrawalResource())
v1_api.register(CashTransferResource())
v1_api.register(ServicesResource())
v1_api.register(ATMCardResource())

urlpatterns = patterns('',
    url(r'^user/$', 'version1.views.main'),
    url(r'^user/card/$', 'version1.views.index'), 
    url(r'^user/validatepin/$', 'version1.views.validatepin'),
    url(r'^user/validatepasscode/$', 'version1.views.validatepasscode'),
    url(r'^user/options/$', 'version1.views.options'),
    url(r'^user/history/$', 'version1.views.history'),    
    url(r'^user/balanceenquiry/$', 'version1.views.balanceenquiry'),
    url(r'^user/cashwithdrawal/$', 'version1.views.cashwithdrawal'),
    url(r'^user/cashtransfer/$', 'version1.views.cashtransfer'),
    url(r'^user/pinchange/$', 'version1.views.pinchange'),
    url(r'^user/phonechange/$', 'version1.views.phonechange'),
    url(r'^user/fastcash/$', 'version1.views.fastcash'),
    url(r'^user/services/$', 'version1.views.services'),
    url(r'^user/exit/$', 'version1.views.exit'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    url(r'^BankServices/rest/biller/$', 'version1.views.services_mock_listBiller'),
    url(r'^admin_user/$', 'version1.views.admin_index'),
    url(r'^admin_user/logout/$', 'version1.views.admin_logout'),
    url(r'^admin_user/verify_user/$', 'version1.views.admin_verify_user'),
    url(r'^admin_user/main_page/$', 'version1.views.admin_main_page'),
    url(r'^admin_user/add_new_card/$', 'version1.views.admin_add_card'),
    url(r'^admin_user/add_atm_operation/$', 'version1.views.admin_add_card_operation'),
    url(r'^admin_user/ATM_status/$', 'version1.views.admin_atm_status'),
    url(r'^admin_user/update_refill/$', 'version1.views.admin_update_refill'),
    url(r'^admin_user/update_card_details/$', 'version1.views.admin_update_card_details'),
    url(r'^admin_user/update_card_details/validate_card/$', 'version1.views.admin_card_validation'),
    url(r'^admin_user/update_card_details/main_page/$', 'version1.views.admin_update_card_main_page'),
    url(r'^admin_user/update_card_details/block_card/$', 'version1.views.admin_block_card'),
    url(r'^admin_user/update_card_details/block_card_operation/$', 'version1.views.admin_block_card_operation'),
    url(r'^admin_user/update_card_details/activate_card/$', 'version1.views.admin_activate_card'),
    url(r'^admin_user/update_card_details/activate_card_operation/$', 'version1.views.admin_activate_card_operation'),
    url(r'^admin_user/update_card_details/reset_pincode/$', 'version1.views.admin_reset_pincode'),
    url(r'^admin_user/update_card_details/reset_pincode_operation/$', 'version1.views.admin_reset_pincode_operation'),
    url(r'^admin_user/update_card_details/reset_phone/$', 'version1.views.admin_reset_phone'),
    url(r'^admin_user/update_card_details/reset_phone_operation/$', 'version1.views.admin_reset_phone_operation'),
    url(r'^admin_user/update_card_details/view_history/$', 'version1.views.admin_view_history'),
    url(r'^admin_user/update_card_details/update_date/$', 'version1.views.admin_update_date'),
    url(r'^admin_user/update_card_details/update_date_operation/$', 'version1.views.admin_update_date_operation'),
)

urlpatterns += staticfiles_urlpatterns()
