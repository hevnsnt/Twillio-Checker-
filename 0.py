# -*- coding: utf-8 -*-
#By CalonMayat 
#Telegram Flavyy7
#Team: PhantomSec1337 

import requests, json
from pyfiglet import figlet_format
from colorama import Fore, Back, Style
import time
import os

merah = Fore.RED
cyan = Fore.CYAN
biru = Fore.BLUE
ijo = Fore.GREEN
kuning = Fore.YELLOW

os.system('clear')
time.sleep(2)

banner = figlet_format("Twillio Checker") 
print (banner) 

print(cyan+" [+] By : CalonMayat") 

print(Style.RESET_ALL)

print(cyan+" [+] Telegram: Flavyy7")

print(Style.RESET_ALL)
time.sleep(3)


def twilio_checker(account_sid, auth_token):
	auth = (account_sid, auth_token)
	try:
		curler_balance = requests.get("https://api.twilio.com/2010-04-01/Accounts/"+account_sid+"/Balance.json", auth=auth).text
		curler_msg = requests.get("https://api.twilio.com/2010-04-01/Accounts/" + account_sid + "/Messages.json", auth=auth).text
		info_balance = json.loads(curler_balance)
		info_msg = json.loads(curler_msg)
		for msg in info_msg["messages"]:
			if msg["direction"] == "outbound-api":
				nope = msg["from"]
				break
			elif msg["direction"] == "inbound-api":
				nope = msg["to"]
				break
		print "Currency: "+info_balance["currency"]
		print "Balance: "+info_balance["balance"]
		print "Phone number: "+nope
	except Exception as err:
		print "ERROR: Invalid credentials"

account_sid = raw_input( merah+" Account sid: ")
auth_token = raw_input( merah+" Auth token: ")
twilio_checker(account_sid, auth_token)
