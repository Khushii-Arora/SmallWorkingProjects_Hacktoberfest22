from django.test import TestCase, Client
from version1.models import *
import simplejson as json
import datetime
import urllib

class MachineTestCase(TestCase):
	'''Tests for the model Machine'''
	def setUp(self):
		'''Set up fields for the test'''
		self.data_1 = Machine(1,"Delhi", 100.00, 500.00, datetime.datetime.now(), datetime.datetime.now())
		self.data_1.save()

	def testMachine(self):
		'''Tests if the fields of model 'Machine' are correctly inserted in the database'''
		self.assertEqual(Machine.objects.all().count(), 1)
		tdata = Machine.objects.get(machine_id = 1)
		self.assertEqual(tdata.location, "Delhi")
		self.assertEqual(tdata.current_balance, 500.00)
		self.assertEqual(tdata.minimum_atm_balance, 100.00)
		self.assertLess(tdata.last_refill_date, datetime.datetime.now())
	
	def testMachine_negative_money(self):
		'''Asserts that updates of negative values to currency are not permitted'''
		temp = self.data_1.current_balance
		self.data_1.current_balance = -100
		self.assertRaises(Exception, self.data_1.save)
		self.data_1 = Machine.objects.get(machine_id = 1)
		self.data_1.minimum_atm_balance = -1
		self.assertRaises(Exception, self.data_1.save)
		self.data_1.minimum_atm_balance = temp
	
	def testMachine_negative_id(self):
		'''Tests negative values for the machine_id field'''
		self.data_1 = Machine.objects.get(machine_id = 1)
		self.data_1.machine_id = -12
		self.assertRaises(Exception, self.data_1.save)

	def testMachine_checkUpdate(self):
		'''Tests if updates to a database entry are done correctly'''
		data = Machine.objects.get(machine_id = 1)
		data.current_balance = 1000.00
		data.save()
		self.assertEqual(Machine.objects.all().count(), 1)

		data_temporary = Machine.objects.get(machine_id = 1)
		self.assertEqual(data_temporary.current_balance, 1000.00)
		data_temporary.minimum_atm_balance = 100.50
		data_temporary.save()
		self.assertEqual(Machine.objects.all().count(), 1)		

		data = Machine.objects.get(machine_id = 1)
		self.assertEqual(data.minimum_atm_balance, 100.50)

class AccountExtensionTestCase(TestCase):
	'''Test cases for the Account_Ext model'''
	def setUp(self):
		'''Set up fields for the test'''
		self.data = Account_Ext(123456789012, "M", 9646818259, 100.00)
		self.data.save()
	
	def testAccountExt(self):
		'''Tests if the fields of model 'Account_Ext' are correctly inserted in the database'''
		self.assertEqual(Account_Ext.objects.all().count(), 1)
		t = Account_Ext.objects.all()[0]
		self.assertEqual(t.acc_num, 123456789012)
		self.assertEqual(t.name, "M")
		self.assertEqual(t.phone_num, 9646818259)
		self.assertEqual(t.balance, 100.00)

	def testAccountExt_negative_fields(self):
		'''Tests if updates of negative values to different fields are not permitted'''
		t = Account_Ext.objects.all()[0]
		t.acc_num = 123
		self.assertRaises(Exception, t.save)

		t = Account_Ext.objects.all()[0]
		t.acc_num = -10
		self.assertRaises(Exception, t.save)

		t = Account_Ext.objects.all()[0]
		t.phone_num = -1245465
		self.assertRaises(Exception, t.save)

		t = Account_Ext.objects.all()[0]
		t.phone_num = 1234
		self.assertRaises(Exception, t.save)

		t = Account_Ext.objects.all()[0]
		t.balance = - 10
		self.assertRaises(Exception, t.save)
	
	def testAccountExt_checkUpdate(self):
		'''Tests if updates to a database entry are done correctly'''
		t = Account_Ext.objects.all()[0]
		t.balance = 12345.00
		t.save()
		self.assertEqual(Account_Ext.objects.all().count(), 1)
		temp = Account_Ext.objects.all()[0]
		
class ATMCardTestCase(TestCase):
	'''Test cases for the ATM_Card model'''
	def setUp(self):
		'''Set up fields for the test'''
		t = Account_Ext(123456789012, "M", 9646818259, 100.00)
		t.save()
		self.data = ATM_Card(account_num=Account_Ext.objects.get(acc_num=123456789012), atmcard_num = 2311, name="M", pin=1234, date_of_issue=datetime.datetime.now(), expiry_date=datetime.datetime(2012, 11, 10, 12, 00), address="12 B, New Delhi", two_factor=False, phone_num=9646818259, card_status=True)		
		self.data.save()

	def testATMCard(self):
		'''Tests if the fields if modes 'ATM_Card' are correctly inserted in the database'''
		self.assertEqual(ATM_Card.objects.all().count(), 1)
		card = ATM_Card.objects.all()[0]
		self.assertEqual(card.account_num_id,123456789012)
		self.assertEqual(card.atmcard_num, 2311)
		self.assertEqual(card.phone_num, 9646818259)
		self.assertEqual(card.card_status, True)
	
	def testATMCard_checkForeignKey(self):
		'''Tests the foreign key constraints for the model'''
		t = ATM_Card.objects.all()[0]
		t.account_num_id = 2
		self.assertRaises(Exception, t.save)
	
	def testATMCard_checkUpdate(self):
		'''Tests if updates to a database entry are done correctly'''
		t = ATM_Card.objects.all()[0]
		t.pin=1212
		t.save()

		self.assertEqual(ATM_Card.objects.all().count(), 1)
		self.assertEqual(ATM_Card.objects.all()[0].pin, 1212)
	
	def testATMCard_invalidFields(self):
		'''Tests if wrong values to different fields are not permitted'''		
		t = ATM_Card.objects.all()[0]
		t.pin = 12
		self.assertRaises(Exception, t.save)

		self.assertEqual(ATM_Card.objects.all().count(), 1)
		t = ATM_Card.objects.all()[0]
		t.atmcard_num = -1234
		self.assertRaises(Exception, t.save)

		self.assertEqual(ATM_Card.objects.all().count(), 1)
		t = ATM_Card.objects.all()[0]
		t.atmcard_num = 'ABC'
		self.assertRaises(Exception, t.save)

		self.assertEqual(ATM_Card.objects.all().count(), 1)
		t = ATM_Card.objects.all()[0]
		t.phone_num = 1234
		self.assertRaises(Exception, t.save)

class ViewsTestCase(TestCase):
	'''Test cases for views'''
	def setUp(self):
		'''Set up fields for the test'''
		self.url = 'http://localhost:8000/'
		self.client = Client()
		self.machine = Machine(1,"Delhi", 500.00, 10000.00, datetime.datetime.now(), datetime.datetime(2012, 2, 2))
		self.machine.save()
		self.account_ext = t = Account_Ext(123456789012, "M", 9646818259, 100.00)
		self.account_ext.save()
		self.atmcard = ATM_Card(account_num=self.account_ext, atmcard_num = 2311, name="M", pin=1234, date_of_issue=datetime.datetime.now(), expiry_date=datetime.datetime(2012, 11, 10, 12, 00), address="12 B, New Delhi", two_factor=False, phone_num=9646818259, card_status=True)
		self.atmcard.save()
	
	def testViews_invalidPages(self):
		'''Tests the response for invalid pages'''
		invalidPages_initial = ['/user/card/', '/user/validatepin', '/user/validatepasscode', '/user/options', '/user/history', '/user/balanceenquiry', '/user/cashwithdrawal', '/user/cashtransfer', '/user/pinchange', '/user/phonechange', '/user/fastcash']
		for page in invalidPages_initial:
			response = self.client.post(page)
			self.assertIn(response.status_code, [301, 302])
	
class APITestCase(TestCase):
	'''Test cases for the API'''
	def setUp(self):
		'''Set up fields for the test'''
		self.url = '/api/v1/'
		self.client = Client()
		self.fields = {'format': 'json'}

	def testAPI_cashwithdrawal(self):
		'''Tests the API for cashwithdrawal'''
		url = self.url + 'cashwithdrawal/'
		res = self.client.get(url + '?' + urllib.urlencode(self.fields))
		response = json.loads(res.content)
		self.assertEqual(response["meta"]["total_count"], 0)

	def testAPI_cashtransfer(self):
		'''Tests the API for cashtransfer'''
		url = self.url + 'cashtransfer/'
		res = self.client.get(url + '?' + urllib.urlencode(self.fields))
		response = json.loads(res.content)
		self.assertEqual(response["meta"]["total_count"], 0)

		Account_Ext(121212121212, "S", 9023043521, 500.00).save()
		acc = Account_Ext(123456789012, "M", 9646818259, 1000.00)
		acc.save()
		atmcard = ATM_Card(account_num=acc, atmcard_num = 2311, name="M", pin=1234, date_of_issue=datetime.datetime.now(), expiry_date=datetime.datetime(2012, 11, 10, 12, 00), address="12 B, New Delhi", two_factor=False, phone_num=9646818259, card_status=True)
		atmcard.save()
		machine = Machine(1,"Delhi", 500.00, 10000.00, datetime.datetime.now(), datetime.datetime(2012, 2, 2))
		machine.save()
		cash = Cash_Transfer(ben_acc_num=121212121212, ben_name="S", amt_trans=125.00, tid = 10, rescode = 3, atmcard_num = atmcard, machine_id = machine, date_time = datetime.datetime.now())
		cash.save()

		res = self.client.get(url + '?' + urllib.urlencode(self.fields))
		response = json.loads(res.content)
		self.assertEqual(response["meta"]["total_count"], 1)
		self.assertEqual(len(response["objects"]), 1)
		self.assertEqual(response["objects"][0]["amt_trans"], 125.00)

	def testAPI_atmcard(self):
		'''Tests the API for atmcard'''
		url = self.url + 'atmcard/'
		res = self.client.get(url + '?' + urllib.urlencode(self.fields))
		response = json.loads(res.content)
		self.assertEqual(response["meta"]["total_count"], 0)
		
		acc = Account_Ext(123456789012, "M", 9646818259, 1000.00)
		acc.save()
		ATM_Card(account_num=acc, atmcard_num = 2311, name="M", pin=1234, date_of_issue=datetime.datetime.now(), expiry_date=datetime.datetime(2012, 11, 10, 12, 00), address="12 B, New Delhi", two_factor=False, phone_num=9646818259, card_status=True).save()
		res = self.client.get(url + '?' + urllib.urlencode(self.fields))
		response = json.loads(res.content)
		self.assertEqual(response["meta"]["total_count"], 1)
						