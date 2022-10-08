# Create your views here.
from version1.models import *
from decimal import *
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect 
import datetime
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
import sys
import random
from django.db.models import Avg, Max, Min, Count
from dateutil.relativedelta import relativedelta
import sms
from lxml import etree
import urllib

##To select the machine
##@param: machineid
##@return: is used to redirect to various pages like '/user/validatepin/','/user/card/','/user/options/'.
@csrf_protect
def main(request):
	if 'cardnumber' in request.session:
		return redirect('/user/validatepin/')  
	if 'pinverified' in request.session:
		return redirect('/user/options/')
	machinelist = Machine.objects.all()
	if len(machinelist) > 0:
		machinelistpresent = True
	if request.method == 'POST':
		print request.POST['m']
		request.session['machine'] = request.POST['m']
		return redirect('/user/card/')   
	return render_to_response('finale/main.html',locals())

##for card validation.
##@param: card number
##@return: is used to redirect to various pages like '/user/validatepin/','/user/card/','/user/'.
@csrf_protect
def index(request):
	if 'machine' not in request.session:
		return redirect('/user/')  
	if 'cardnumber' in request.session:
		return redirect('/user/validatepin/')  
		
	if request.method == 'POST':
		cardnum = request.POST['cardnumber']
		try:
			card = ATM_Card.objects.filter(atmcard_num=cardnum)
			if not card:
				cmessage=1
			elif not card[0].card_status:
				cmessage=2
			else:
				date = datetime.datetime.now()
				if(card[0].expiry_date < date):
					cmessage=3
				else:
					request.session['cardnumber'] = cardnum  
					return redirect('/user/validatepin/')
		except:
			e = sys.exc_info()[1]
			cmessage=1	   
	return render_to_response('finale/index.html',locals())   

##for pin validation and messaging two factor verification code to registered phone no. of card holder(if two facto enabled).
##@param: pincode and phoneno(if needed)
##@return: is used to redirect to various pages like '/user/validatepin/','/user/card/','/user/'  and '/user/options/'.
@csrf_protect
def validatepin(request):
	if 'machine' not in request.session:
		return redirect('/user/')
	if 'cardnumber' not in request.session:  
		return redirect('/user/card/')
	if 'pinverified' in request.session:       
		return redirect('/user/options/')
	atmcard = ATM_Card.objects.get(atmcard_num=request.session['cardnumber'])
	username = atmcard.name
	request.session['username'] = username        
	
	if request.method == 'POST': 
		try:
			cardpin = request.POST['pincode']         
			if int(atmcard.pin) == int(cardpin):         
				request.session['pinverified'] = True
				request.session.set_expiry(300)

				if atmcard.two_factor:
					request.session['passcode']=random.randint(1000,9999)
					print request.session['passcode']
					sms.sendSMS(atmcard.phone_num, 'PASSCODE:%d' % request.session['passcode'])
					return redirect('/user/validatepasscode')       
				return redirect('/user/options')
			if 'pinattempt' not in request.session:
				request.session['pinattempt'] = 1
			else:
				request.session['pinattempt'] = request.session['pinattempt'] + 1
			
			if request.session['pinattempt'] == 1:
					pinmessage = 1
			elif request.session['pinattempt'] == 2:
					pinmessage = 2
			else:
					pinmessage = 3
					atmcard.card_status = False
					atmcard.save()
					request.session.flush()
		except:
			e = sys.exc_info()[1]
			if 'pinattempt' not in request.session:
				request.session['pinattempt'] = 1
			else:
				request.session['pinattempt'] = request.session['pinattempt'] + 1
			if request.session['pinattempt'] == 1:
					pinmessage = 1
			elif request.session['pinattempt'] == 2:
					pinmessage = 2
			else:
					pinmessage = 3
					atmcard.card_status = False
					atmcard.save()
					request.session.flush()	  			
	return render_to_response('finale/pincode.html', locals())

##for passcode validation(if enabled).
##@param: two factor verification code
##@return: is used to redirect to various pages like '/user/card/','/user/'  and '/user/options/'.
@csrf_protect
def validatepasscode(request):
	if 'machine' not in request.session:
		return redirect('/user/')
	if 'cardnumber' not in request.session:  
		return redirect('/user/card/')
	atmcard = ATM_Card.objects.get(atmcard_num=request.session['cardnumber'])	
	if 'pinverified' in request.session and not atmcard.two_factor:       
		return redirect('/user/options/')
	if 'passcodeverified' in request.session:       
		return redirect('/user/options/')
	username = atmcard.name
	request.session['username'] = username        
	no = atmcard.phone_num
	if request.method == 'POST': 
		try:
			passcode = request.POST['passcode']         
			if int(request.session['passcode']) == int(passcode):         
				request.session['passcodeverified'] = True       
				return redirect('/user/options')
			if 'passattempt' not in request.session:
				request.session['passattempt'] = 1
			else:
				request.session['passattempt'] = request.session['passattempt'] + 1
			
			if request.session['passattempt'] == 1:
					pinmessage = 1
			elif request.session['passattempt'] == 2:
					pinmessage = 2
			else:
					pinmessage = 3
					request.session.flush()
		except:
			e = sys.exc_info()[1]
			if 'passattempt' not in request.session:
				request.session['passattempt'] = 1
			else:
				request.session['passattempt'] = request.session['passattempt'] + 1
			if request.session['passattempt'] == 1:
					pinmessage = 1
			elif request.session['passattempt'] == 2:
					pinmessage = 2
			else:
					pinmessage = 3
					request.session.flush()	  			
	return render_to_response('finale/passcode.html', locals())

##it shows the various options available to user
##@param: 'request' stores which form method we are using i.e(GET/POST) and session variable
##@return: is used to redirect to various pages like '/user/pinvalidation/','/user/card/','/user/'  and '/user/options/'.
@csrf_protect
def options(request):
	if 'machine' not in request.session:
		return redirect('/user/')
	if 'cardnumber' not in request.session:
		return redirect('/user/card/')
	if 'pinverified' not in request.session:
		return redirect('/user/pinvalidation/')
	print request.session.get_expiry_age()
	username = request.session['username']
	return render_to_response('finale/options.html', locals())

##To show the balance to cardholder and saves the transaction in database.
##@param: 'request' stores which form method we are using i.e(GET/POST) and session variable
##@return: is used to redirect to various pages like '/user/validatepin/','/user/card/','/user/'  and '/user/options/'.
@csrf_protect
def balanceenquiry(request):
	if 'machine' not in request.session:
		return redirect('/user/')
	if 'cardnumber' not in request.session:
		return redirect('/user/card/')
	if 'pinverified' not in request.session:
		return redirect('/user/pinvalidation/')	
	atmcard = ATM_Card.objects.get(atmcard_num=request.session['cardnumber'])
	t_acc = Account_Ext.objects.get(acc_num=str(atmcard.account_num))
	t = Balance_Enquiry(atmcard_num = atmcard, machine_id_id = request.session['machine'],tid = 1,date_time = datetime.datetime.now(),status = "Completed",rescode = 1,type_trans = "Balance Enquiry",bal_amount=t_acc.balance)
	t.save()
	bal = t_acc.balance
	username=atmcard.name
	return render_to_response('finale/balance.html', locals())

##To withdraw the money from machine and saves the transaction in database.
##@param: withdrawal amount
##@return: is used to redirect to various pages like '/user/validatepin/','/user/card/','/user/'  and '/user/options/'.
@csrf_protect	
def cashwithdrawal(request):
	if 'machine' not in request.session:
		return redirect('/user/')
	if 'cardnumber' not in request.session:
		return redirect('/user/card/')
	if 'pinverified' not in request.session:
		return redirect('/user/pinvalidation/')
	username=request.session['username']
	if request.method == 'POST':
		try:
			atmcard = ATM_Card.objects.get(atmcard_num=request.session['cardnumber'])
			t_acc = Account_Ext.objects.get(acc_num=str(atmcard.account_num))
			if(Decimal(t_acc.balance)>Decimal(request.POST['amount'])):
				t_acc.balance = t_acc.balance - Decimal(request.POST['amount'])
				t_acc.save()
				t = Cash_Withdrawl(atmcard_num = atmcard, machine_id_id = request.session['machine'],tid = 1,date_time = datetime.datetime.now(),status = "Completed",rescode = 2,type_trans = "Cash Withdrawal",amt_with = Decimal(request.POST['amount']),cur_bal=t_acc.balance)
				t.save()
				wdmessage = 1
			else:
				ta = Cash_Withdrawl(atmcard_num = atmcard, machine_id_id =request.session['machine'], tid = 1, date_time = datetime.datetime.now(),status = "Not Completed",rescode = 11,type_trans = "Cash Withdrawal",amt_with = Decimal(request.POST['amount']),cur_bal = t_acc.balance)
				ta.save()
				wdmessage = 2
		except:
			e = sys.exc_info()[1]
			wdmessage=3		
	return render_to_response('finale/cashwithdrawal.html', locals())

##To transfer the cash from cardholder's account to another specified account and saves the transaction in database.
##@param: name and account no. in which we want to transfer the money and amount to transfer.
##@return: is used to redirect to various pages like '/user/pinvalidation/','/user/card/','/user/'  and '/user/options/'.
@csrf_protect	
def cashtransfer(request):
	if 'machine' not in request.session:
		return redirect('/user/')
	if 'cardnumber' not in request.session:
		return redirect('/user/card/')
	if 'pinverified' not in request.session:
		return redirect('/user/pinvalidation/')
	username=request.session['username']
	if request.method == 'POST':
		try:
			accnum = request.POST['acc_num']
			accname = request.POST['name']
			acc_2 = Account_Ext.objects.filter(acc_num=accnum,name=accname)
			if not acc_2:
				ctmessage = 0
			else:
				atmcard = ATM_Card.objects.get(atmcard_num=request.session['cardnumber'])
				t_acc = Account_Ext.objects.get(acc_num=str(atmcard.account_num))
				if(Decimal(t_acc.balance)>Decimal(request.POST['amount'])):
					t_acc.balance = t_acc.balance - Decimal(request.POST['amount'])
					t_acc.save()
					acc_2[0].balance = acc_2[0].balance + Decimal(request.POST['amount'])
					acc_2[0].save()
					t = Cash_Transfer(atmcard_num = atmcard, machine_id_id = request.session['machine'],tid = 1,date_time = datetime.datetime.now(),status = "Completed",rescode = 3,type_trans = "Cash Transfer",amt_trans = Decimal(request.POST['amount']),ben_acc_num=accnum,ben_name=accname)
					t.save()
					ctmessage = 1
				else:
					ta = Cash_Transfer(atmcard_num = atmcard, machine_id_id = request.session['machine'], tid = 1, date_time = datetime.datetime.now(),status = "Not Completed",rescode = 12,type_trans = "Cash Transfer",amt_trans = Decimal(request.POST['amount']),ben_acc_num=accnum,ben_name=accname)
					ta.save()
					ctmessage = 2		
		except:
			e = sys.exc_info()[1]
			ctmessage=3	
	return render_to_response('finale/cashtransfer.html', locals())

##To change the pin and saves the transaction in database.
##@param: previous pincode,new pincode,confirm pincode
##@return: is used to redirect to various pages like '/user/validatepin/','/user/card/','/user/'  and '/user/options/'.
@csrf_protect
def pinchange(request):
	if 'machine' not in request.session:
		return redirect('/user/')
	if 'cardnumber' not in request.session:
		return redirect('/user/card/')
	if 'pinverified' not in request.session:
		return redirect('/user/pinvalidation/')
	username = request.session['username']
	if request.method == 'POST':
		try:
			atmcard = ATM_Card.objects.get(atmcard_num=request.session['cardnumber'])
			cardpin = request.POST['pincode']
			npin = request.POST['npincode']
			cpin = request.POST['cpincode']
			if int(atmcard.pin) == int(cardpin):
				if int(npin) == int(cpin):
					if int(atmcard.pin) == int(cpin):
						#same no need to do any thing
						pcmessage=1
					else:
						#successfull
						pcmessage=4
						t = Pin_change(atmcard_num = atmcard, machine_id_id = request.session['machine'],tid = 1,date_time = datetime.datetime.now(),status = "Completed",rescode = 4,type_trans = "Pin Change",prev_pin=cardpin,new_pin=npin)
						t.save()
						atmcard.pin=int(cpin)
						atmcard.save() 
							
				else:
					#new pin and confirm pin are different
					pcmessage=2
				
			else:
				#invalid pincode
				pcmessage=3
		except:
			e = sys.exc_info()[1]
			pcmessage=5			
	return render_to_response('finale/pinchange.html', locals())	

##To change the phoneno. and saves the transaction in database.
##@param: new phoneno and confirm phoneno
##@return: is used to redirect to various pages like '/user/validatepin/','/user/card/','/user/'  and '/user/options/'.
@csrf_protect	
def phonechange(request):
	if 'machine' not in request.session:
		return redirect('/user/')
	if 'cardnumber' not in request.session:
		return redirect('/user/card/')
	if 'pinverified' not in request.session:
		return redirect('/user/pinvalidation/')
	username = request.session['username']
	if request.method == 'POST':
		try:
			atmcard = ATM_Card.objects.get(atmcard_num=request.session['cardnumber'])
			nphone = request.POST['nphone']
			cphone = request.POST['cphone']
			if int(nphone) == int(cphone):
					if int(atmcard.phone_num) == int(cphone):
						#same no need to do any thing
						pcmessage=1
					else:
						#successfull
						pcmessage=4
						t = Phone_change(atmcard_num = atmcard, machine_id_id = request.session['machine'],tid = 1,date_time = datetime.datetime.now(),status = "Completed",rescode = 4,type_trans = "Pin Change",prev_phone=atmcard.phone_num,new_phone=nphone)
						t.save()
						atmcard.phone_num=int(cphone)
						atmcard.save() 
							
			else:
				#new phoneno and confirm phoneno are different
				pcmessage=2
		except:
			e = sys.exc_info()[1]
			pcmessage=5
			
	return render_to_response('finale/phonechange.html', locals())

##To withdraw the money by just selecting one of the option available to cardholder and saves the transaction in database.
##@param: selected amount
##@return: is used to redirect to various pages like '/user/validatepin/','/user/card/','/user/'  and '/user/options/'.
@csrf_protect	
def fastcash(request):
	if 'machine' not in request.session:
		return redirect('/user/')
	if 'cardnumber' not in request.session:
		return redirect('/user/card/')
	if 'pinverified' not in request.session:
		return redirect('/user/pinvalidation/')
	username=request.session['username']
	if request.method == 'POST':
		try:
			atmcard = ATM_Card.objects.get(atmcard_num=request.session['cardnumber'])
			t_acc = Account_Ext.objects.get(acc_num=str(atmcard.account_num))
			if(Decimal(t_acc.balance)>Decimal(request.POST['fcash'])):
				t_acc.balance = t_acc.balance - Decimal(request.POST['fcash'])
				t_acc.save()
				t = Cash_Withdrawl(atmcard_num = atmcard, machine_id_id = request.session['machine'],tid = 1,date_time = datetime.datetime.now(),status = "Completed",rescode = 2,type_trans = "Cash Withdrawal",amt_with = Decimal(request.POST['fcash']),cur_bal=t_acc.balance)
				t.save()
				fcmessage = 1
				request.session.flush()
			else:
				ta = Cash_Withdrawl(atmcard_num_id = request.session['cardnumber'], machine_id_id =request.session['machine'], tid = 1, date_time = datetime.datetime.now(),status = "Not Completed",rescode = 11,type_trans = "Cash Withdrawal",amt_with = Decimal(request.POST['fcash']),cur_bal = t_acc.balance)
				ta.save()
				fcmessage = 2
		except:
			e = sys.exc_info()[1]
			fcmessage=3		
	return render_to_response('finale/fastcash.html', locals())

##To show the history of successfull transactions(only involving money) made by cardholder and saves the transaction in database.
##@param: 'request' stores which form method we are using i.e(GET/POST) and session variable
##@return: is used to redirect to various pages like '/user/validatepin/','/user/card/','/user/'  and '/user/options/'.
@csrf_protect
def history(request):
	if 'machine' not in request.session:
		return redirect('/user/')
	if 'cardnumber' not in request.session:
		return redirect('/user/card/')
	if 'pinverified' not in request.session:
		return redirect('/user/pinvalidation/')
	username = request.session['username']
	cardnum=request.session['cardnumber']
	cashw=Cash_Withdrawl.objects.filter(atmcard_num=cardnum,rescode=2)
	casht=Cash_Transfer.objects.filter(atmcard_num=cardnum,rescode=3)
	list_transaction=[]
	
	for e in cashw:
		dict={}
		dict['date'] = e.date_time
		dict['tt'] = e.type_trans
		dict['amount'] =e.amt_with
		list_transaction.append(dict)
	for e in casht:
		dict={}
		dict['date'] = e.date_time
		dict['tt'] = e.type_trans
		dict['amount'] =e.amt_trans
		list_transaction.append(dict)	
	return render_to_response('finale/history.html', locals())

def services_mock_listBiller(request):
	r = etree.Element('BankServices')
	billers = etree.SubElement(r, 'Billers')
	
	b1 = etree.SubElement(billers, 'Biller', category="MutualFunds")
	etree.SubElement(b1, 'name').text = "LIC"
	etree.SubElement(b1, 'account_id').text = "201"
	
	b1 = etree.SubElement(billers, 'Biller', category="Water")
	etree.SubElement(b1, 'name').text = "Delhi Jal Board"
	etree.SubElement(b1, 'account_id').text = "202" 

	b1 = etree.SubElement(billers, 'Biller', category="Telephone")
	etree.SubElement(b1, 'name').text = "Airtel"
	etree.SubElement(b1, 'account_id').text = "203"

	b1 = etree.SubElement(billers, 'Biller', category="Telephone")
	etree.SubElement(b1, 'name').text = "MTNL"
	etree.SubElement(b1, 'account_id').text = "204"

	b1 = etree.SubElement(billers, 'Biller', category="Exam")
	etree.SubElement(b1, 'name').text = "GATE"
	etree.SubElement(b1, 'account_id').text = "205"

	b1 = etree.SubElement(billers, 'Biller', category="Electricity")
	etree.SubElement(b1, 'name').text = "Delhi Electricity Board"
	etree.SubElement(b1, 'account_id').text = "206"

	b1 = etree.SubElement(billers, 'Biller', category="Exam")
	etree.SubElement(b1, 'name').text = "IIT JEE"
	etree.SubElement(b1, 'account_id').text = "207"

	return HttpResponse(etree.tostring(r), mimetype="text/xml")

@csrf_protect
def services(request):
	if 'machine' not in request.session:
		return redirect('/user/')
	if 'cardnumber' not in request.session:
		return redirect('/user/card/')
	if 'pinverified' not in request.session:
		return redirect('/user/pinvalidation/')	
	r = urllib.urlopen('http://localhost:8000/BankServices/rest/biller')
	print r.read()
	serv = etree.parse(r.read())	
	serviceslist = root.iter()
	return render_to_response('finale/services.html', locals())

##To delete the session.
##@param: 'request' stores which form method we are using i.e(GET/POST) and session variable
##@return: is used to redirect to various pages like '/user/pinvalidation/','/user/card/' and '/user/'.	
@csrf_protect
def exit(request):
	if 'machine' not in request.session:
		return redirect('/user/')
	if 'cardnumber' not in request.session:
		return redirect('/user/card/')
	if 'pinverified' not in request.session:
		return redirect('/user/pinvalidation/')
	request.session.flush()
	return redirect('/user/')

## admin_index() displays the index page of the administrator where he will be asked to fill the user name and password 
@csrf_protect
def admin_index(request): 	
	return render_to_response('admin_user/index.html', locals())
    
## admin_verify_user() user will verify the administrator and password entered by him
## this function also starts the session for the Administrator if username and password are entered correctly   
##@param: username and password of admin   
@csrf_protect
def admin_verify_user(request):
	if request.method == 'POST':
		admin=Admin.objects.filter(Admin_id=request.POST['username'],Password=request.POST['password'])
		if not admin:
			failed=True
			return render_to_response('admin_user/index.html', {"failed":failed})#locals())
		else:	 	
			request.session['login'] = True
			return render_to_response('admin_user/main_page.html',locals())
	else:
		return redirect('/admin_user/')	
		
## admin_main_page() displays all the option for the administrator 		
def admin_main_page(request): 
	if 'login' not in request.session:
		return render_to_response('admin_user/index.html', locals())
	else:
		return render_to_response('admin_user/main_page.html', locals())
		
		
## admin_add_card() displays the page which asks for card details
def admin_add_card(request):
	if 'login' not in request.session:
		return render_to_response('admin_user/index.html', locals())
	else:
		acc_list = Account_Ext.objects.all()	
		return render_to_response('admin_user/add_atm.html',{"acc_list":acc_list})

## admin_add_card_operation() creates new ATM card
##@param: account no.,phoneno.,name,address,twofactorverification		
def admin_add_card_operation(request):
	if 'login' not in request.session:
		return render_to_response('admin_user/index.html', locals())
	else:
		try:
			if ((request.GET['phone']=="") or (request.GET['address']=="")or (request.GET['pin']=="") or (request.GET['name']=="")):
				empty=True 
				return render_to_response('admin_user/view_atm_status.html', {"Machine_list":Machine_list}, {"empty":empty})
			else:
				if (request.GET['two']=='False'):
					t=False
				else: 
					t=True
				p=datetime.datetime.now()
				q =p + relativedelta(years=+4)
				e = ATM_Card(atmcard_num=(1111+random.randint(1000,8888)),account_num_id=request.GET['acc'],name=request.GET['name'],pin=request.GET['pin'],date_of_issue=p,expiry_date=q,address=request.GET['address'],two_factor=t,phone_num=request.GET['phone'],card_status=True)
				e.save()
				return render_to_response('admin_user/main_page.html',locals())
		except Exception as e:
				acc_list = Account_Ext.objects.all()	
				m=True
				#return: render_to_response('admin_user/index.html', locals())
				return render_to_response('admin_user/add_atm.html',locals())
				 
# admin_atm_status() will show the details of all the ATM-machines 
def admin_atm_status(request):
	if 'login' not in request.session:
		return render_to_response('admin_user/index.html', locals())
	else:
		Machine_list = Machine.objects.all()
		return render_to_response('admin_user/view_atm_status.html', {"Machine_list":Machine_list})	

# admin_update_refill() will send a request to the autority to fill the refill of that ATM machine		
def admin_update_refill(request):
	if 'login' not in request.session:
		return render_to_response('admin_user/index.html', locals())
	else:
		[machine] =Machine.objects.filter(machine_id=request.GET['id'])
		date_time = datetime.datetime.now()
		machine.next_maintainence_date=date_time
		machine.save()
		Machine_list = Machine.objects.all()
		return render_to_response('admin_user/view_atm_status.html', {"Machine_list":Machine_list})

## admin_update_card_details will ask the administrator to enter the atm card number which he want to update
def admin_update_card_details(request):
	if 'login' not in request.session:
		return render_to_response('admin_user/index.html', locals())
	else:
		return render_to_response('admin_user/enter_card_no.html', locals())	

## admin_card_validation() will validate the atm card no and it is correct then it will take the administrator to options else it will dispay that card is not valid
##@param: cardnumber
def admin_card_validation(request):
	if 'login' not in request.session:
		return render_to_response('admin_user/index.html', locals())
	else:
		try:
			if request.method == 'POST':
				[cardcheck] =ATM_Card.objects.filter(atmcard_num=request.POST['cardnumber'])
				if not cardcheck:
					failed=True
					return render_to_response('admin_user/enter_card_no.html', {"failed":failed})	
				else:			 	
					#card=cardcheck
					request.session['admin_session_card'] = request.POST['cardnumber']
					request.session['admin_session']=1
					return render_to_response('admin_user/update_card_details.html', locals())
		except Exception as e:
				m=True 
				return render_to_response('admin_user/enter_card_no.html', {"m":m})

## admin_update_card_main_page() displays all the options on the screen for the administrator too update the card details		
def	admin_update_card_main_page(request):
	if 'login' not in request.session:
		return render_to_response('admin_user/index.html', locals())
	else:
		if 'admin_session' not in request.session:
			return render_to_response('admin_user/enter_card_no.html', locals())
		else:			
			return render_to_response('admin_user/update_card_details.html', locals())
			
## admin_block_card() displays the page on which we can block the card		
def admin_block_card(request):
	if 'login' not in request.session:
		return render_to_response('admin_user/index.html', locals())
	else:
		if 'admin_session' not in request.session:
			return render_to_response('admin_user/enter_card_no.html', locals())
		else:			
			return render_to_response('admin_user/block_card.html', locals())

## admin_block_card() blocks the ATM card and saves in the database.	
def admin_block_card_operation(request):
	if 'login' not in request.session:
		return render_to_response('admin_user/index.html', locals())
	else:
		if 'admin_session' not in request.session:
			return render_to_response('admin_user/enter_card_no.html', locals())
		else:			
			[cardcheck] =ATM_Card.objects.filter(atmcard_num=request.session['admin_session_card'])
			cardcheck.card_status=False
			cardcheck.save()
			return render_to_response('admin_user/update_card_details.html', locals())	
			
## admin_activate_card() displays the page which asks for confirmation of the administrator to activate the ATM card
def admin_activate_card(request):
	if 'login' not in request.session:
		return render_to_response('admin_user/index.html', locals())
	else:
		if 'admin_session' not in request.session:
			return render_to_response('admin_user/enter_card_no.html', locals())
		else:			
			return render_to_response('admin_user/activate_card.html', locals())	
		
## admin_activates_card() activates the ATM card by changing status to true in database		
def admin_activate_card_operation(request):
	if 'login' not in request.session:
		return render_to_response('admin_user/index.html', locals())
	else:
		if 'admin_session' not in request.session:
			return render_to_response('admin_user/enter_card_no.html', locals())
		else:			
			[cardcheck] =ATM_Card.objects.filter(atmcard_num=request.session['admin_session_card'])
			cardcheck.card_status=True
			cardcheck.save()
			return render_to_response('admin_user/update_card_details.html', locals())	
			
## admin_reset_pincode() displays the page which aks the administrator to enter the new pin		
def admin_reset_pincode(request):
	if 'login' not in request.session:
		return render_to_response('admin_user/index.html', locals())
	else:
		if 'admin_session' not in request.session:
			return render_to_response('admin_user/enter_card_no.html', locals())
		else:			
			return render_to_response('admin_user/reset_pin.html', locals())	
			

## admin_reset_phone() displays the page from which adminstrator can change the pincode of cardholder	
##@param: new pincode and confirm pincode
def admin_reset_pincode_operation(request):
	if 'login' not in request.session:
		return render_to_response('admin_user/index.html', locals())
	else:
		if 'admin_session' not in request.session:
			return render_to_response('admin_user/enter_card_no.html', locals())
		else:
			try:
				if ((request.GET['password1']=="") or (request.GET['password2']=="")):
					empty=True 
					return render_to_response('admin_user/reset_pin.html', {"empty":empty})		
				else:
					if (request.GET['password1']==request.GET['password2']):			
						[cardcheck] =ATM_Card.objects.filter(atmcard_num=request.session['admin_session_card'])
						cardcheck.pin=request.GET['password1']
						cardcheck.save()
						return render_to_response('admin_user/update_card_details.html', locals())	
					else:
						match=True 
						return render_to_response('admin_user/reset_pin.html', {"match":match})
			except Exception as e:
				m=True 
				return render_to_response('admin_user/reset_pin.html', {"m":m})

## admin_reset_phone() displays the page from which adminstrator can change the phone				
def admin_reset_phone(request):
	if 'login' not in request.session:
		return render_to_response('admin_user/index.html', locals())
	else:
		if 'admin_session' not in request.session:
			return render_to_response('admin_user/enter_card_no.html', locals())
		else:			
			return render_to_response('admin_user/reset_phone.html', locals())	

## admin_reset_phone_operation() reset the phone to new phone enetered by the administrator
##@param: new phoneno, confirm phoneno.			
def admin_reset_phone_operation(request):
	if 'login' not in request.session:
		return render_to_response('admin_user/index.html', locals())
	else:
		if 'admin_session' not in request.session:
			return render_to_response('admin_user/enter_card_no.html', locals())
		else:
			try:
				if ((request.GET['phone1']=="") or (request.GET['phone2']=="")):
					empty=True 
					return render_to_response('admin_user/reset_phone.html', {"empty":empty})		
				else:
					if (request.GET['phone1']==request.GET['phone2']):			
						[cardcheck] =ATM_Card.objects.filter(atmcard_num=request.session['admin_session_card'])
						cardcheck.phone_num=request.GET['phone1']
						cardcheck.save()
						return render_to_response('admin_user/update_card_details.html', locals())	
					else:
						match=True 
						return render_to_response('admin_user/reset_phone.html', {"match":match})	
			except Exception as e:
				m=True 
				return render_to_response('admin_user/reset_phone.html', {"m":m})			 
	
## admin_view_history() shows the previous history of the ATM card 									
def admin_view_history(request):
	
	if 'login' not in request.session:
		return render_to_response('admin_user/index.html', locals())
	else:
		if 'admin_session' not in request.session:
			return render_to_response('admin_user/enter_card_no.html', locals())
		else:
			cardnum=request.session['admin_session_card']
			cashw=Cash_Withdrawl.objects.filter(atmcard_num=cardnum)
			print cashw
			casht=Cash_Transfer.objects.filter(atmcard_num=cardnum)
			print casht
			bal = Balance_Enquiry.objects.filter(atmcard_num=cardnum)
			print bal
			pin = Pin_change.objects.filter(atmcard_num=cardnum)
			print pin
			phone = Phone_change.objects.filter(atmcard_num=cardnum)
			print phone
			list_transaction=[]
			
			for e in cashw:
				dict={}
				dict['date'] = e.date_time
				dict['tt'] = e.type_trans
				dict['amount'] = e.amt_with
				dict['status'] = e.status
				list_transaction.append(dict)
			for e in casht:
				dict={}
				dict['date'] = e.date_time
				dict['tt'] = e.type_trans
				dict['amount'] =e.amt_trans
				dict['status'] = e.status
				list_transaction.append(dict)
			for e in bal:
				dict={}
				dict['date'] = e.date_time
				dict['tt'] = e.type_trans
				dict['amount'] = 'NOT APLLICABLE'
				dict['status'] = e.status
				list_transaction.append(dict)
			for e in pin:
				dict={}
				dict['date'] = e.date_time
				dict['tt'] = e.type_trans
				dict['amount'] = 'NOT APLLICABLE'
				dict['status'] = e.status
				list_transaction.append(dict)	
			for e in phone:
				dict={}
				dict['date'] = e.date_time
				dict['tt'] = e.type_trans
				dict['amount'] = 'NOT APLLICABLE'
				dict['status'] = e.status
				list_transaction.append(dict)		
								
			return render_to_response('admin_user/view_history.html', locals())	
			
##admin_update_date() displays the page from which admin can update the expiry date of card holder			
def admin_update_date(request):
	if 'login' not in request.session:
		return render_to_response('admin_user/index.html', locals())
	else:
		if 'admin_session' not in request.session:
			return render_to_response('admin_user/enter_card_no.html', locals())
		else:			
			return render_to_response('admin_user/update_expiring_date.html', locals())
			
## admin_update_date_operation() update the expiring date in the database by 4 years		
def admin_update_date_operation(request):

	if 'login' not in request.session:
		return render_to_response('admin_user/index.html', locals())
	else:
		if 'admin_session' not in request.session:
			return render_to_response('admin_user/enter_card_no.html', locals())
		else:							
			[cardcheck] =ATM_Card.objects.filter(atmcard_num=request.session['admin_session_card'])
			t=cardcheck.expiry_date
			t += relativedelta(years=+4)
			cardcheck.expiry_date=t
			cardcheck.save()
			return render_to_response('admin_user/update_card_details.html', locals())	

##admin_logout() logsout the administrator and deletes the session.
def admin_logout(request):
	for sesskey in request.session.keys():
		del request.session[sesskey]
	return render_to_response('admin_user/index.html', locals())
