import pywhatkit as whatsapp_kit
import pyautogui as whatsapp_act
from .models import *

import datetime

time_call=datetime.datetime.now()
print(f"the date time {str(time_call.hour)}:{str(time_call.minute)}:{str(time_call.second)}")

def call_message():

 try:
      
      whatsapp_kit.sendwhatmsg("+201094128969","BLUE EYES WHITE DRAGON X2",time_call.hour,time_call.minute+1)
      whatsapp_act.press("send",1,0,False,False)
      print("msg sent")
 except:
      print("ERROR OCCOUR ...... msg was not sent")







def make_a_checkout(business_mail,item_price,item_name,invoice_code,currency_country,info_pay_url,win_pay_url,fall_pay_url,):
      print("\n\nthis function returns a dictionary\n\n")
      view_payment_status={
            'business':business_mail,
            'amount':item_price,
            'item_name':item_name,
            'invoice':invoice_code,
            'currency_code':currency_country,
            'notify_url':info_pay_url,
            'return_url':win_pay_url,
            'cancel_url':fall_pay_url,
      }
      return view_payment_status

def get_Razorpay_data(amountx,currency,rz_client):
    print("\nobtaining the required data\n")
    amount=amountx
    order_currency=currency
    payment=rz_client.order.create({'amount':amount,'currency':currency,'payment_capture':'1',})





def users_registerd_this_day():pass