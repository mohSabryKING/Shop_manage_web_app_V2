from typing import Any, Mapping
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import *
from django import forms 
from django.contrib.auth.forms import *

from django.contrib.auth.models import User
from paypal.standard.forms import PayPalPaymentsForm





class Add_user_form(UserCreationForm):
    class Meta:
        model = User
        fields =('username','password1','password2')

class Make_UserProfile_form(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         self.fields["img_user"].widget.attrs.update({"class": "special",'onClick':'get_user_img("id_img_user","show_user_img");'})
         self.fields["img_bkg"].widget.attrs.update({"class": "special",'onClick':'get_user_img("id_img_bkg","show_bkg");'})
    
    class Meta:
        model = User_profile_model
        fields =('p_name','p_type','img_user','img_bkg','user_phone')
        widgets={'owned_by':forms.HiddenInput(),} 
        
        





class Trader_activity_form(forms.ModelForm):
    class Meta:
        model = Trader_model
        fields = ('t_name','address','branch_locat','des')
        
        widgets={'owned_by':forms.HiddenInput()}



class Add_a_Goods_model_form(forms.ModelForm):
    #'owned_by','name','p_type','img_prod','des','discount_precent','amount','price_after_discount'
    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         self.fields["img_prod"].widget.attrs.update({'onClick':'get_user_img("id_img_prod", "show_prod_img")'})
    
    class Meta:
        model = Goods_model
        fields = ('name','img_prod','des','discount_precent','price','amount','always_avil')
        widgets={'owned_by':forms.HiddenInput(), }


class Add_restaurant_model(forms.ModelForm):
    #owned_by,r_name,branch_locat,user_phone
      
    class Meta:
        model = Restaurant_model
        fields = ('owned_by','r_name','img_locat','address','branch_locat','des')
        widgets={'owned_by':forms.HiddenInput()}


class Add_Service_company_model(forms.ModelForm):
    #owned_by,r_name,branch_locat,user_phone
      
    class Meta:
        model = Service_provider_model
        fields = ('owned_by','company_name','img_logo','address','branch_locat')
        widgets={'owned_by':forms.HiddenInput()}



class Add_Service_model(forms.ModelForm):
    #owned_by,r_name,branch_locat,user_phone
      
    class Meta:
        model = Service_model
        fields = ('owned_by','provider','name','img_serve','price','des')
        widgets={'owned_by':forms.HiddenInput(),'provider':forms.HiddenInput(),}




class Pay_Now_order(PayPalPaymentsForm):

    def get_html_submit_element(self):
        return """<button class='btn_v1' type="submit">شراء مباشر</button>"""
