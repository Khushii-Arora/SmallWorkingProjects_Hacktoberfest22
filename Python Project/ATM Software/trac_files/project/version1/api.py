# version1/api.py
from tastypie.resources import ModelResource
from version1.models import Cash_Withdrawl, Cash_Transfer, Services, ATM_Card

class CashWithdrawalResource(ModelResource):
	class Meta:
		queryset = Cash_Withdrawl.objects.filter(rescode=2)
		resource_name = 'cashwithdrawal'

class CashTransferResource(ModelResource):
	class Meta:
		queryset = Cash_Transfer.objects.filter(rescode=3)
		resource_name = 'cashtransfer'		

class ServicesResource(ModelResource):
	class Meta:
		queryset = Cash_Transfer.objects.filter(rescode=101)
		resource_name = 'service'
		
class ATMCardResource(ModelResource):
	class Meta:
		queryset = ATM_Card.objects.all()
		resource_name = 'atmcard'
		excludes = ['pin', 'expiry_date']