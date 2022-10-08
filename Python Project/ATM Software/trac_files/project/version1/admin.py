from version1.models import Admin
from version1.models import Machine
from version1.models import MachineRefill
from version1.models import Account_Ext
from version1.models import ATM_Card
from version1.models import Balance_Enquiry
from version1.models import Cash_Transfer
from version1.models import Cash_Withdrawl
from version1.models import Pin_change
from version1.models import Phone_change
from django.contrib import admin

admin.site.register(Admin)
admin.site.register(Machine)
admin.site.register(MachineRefill)
admin.site.register(Account_Ext)
admin.site.register(ATM_Card)
admin.site.register(Balance_Enquiry)
admin.site.register(Cash_Transfer)
admin.site.register(Cash_Withdrawl)
admin.site.register(Pin_change)
admin.site.register(Phone_change)
