from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic.base import TemplateView

from django.views.generic.edit import *
#from django.views.generic import *
from django.urls import *
from django.contrib.auth.models import *
from django.contrib.auth import login
from .forms import *
import razorpay

from paypal.standard.forms import PayPalPaymentsForm
import uuid as u_pay_key
from django.shortcuts import *
from django.conf import *
from .Act_1 import *
from shop_manage.settings import *
import stripe
# Create your views here.


class Menu(TemplateView):
    template_name='home.html'
    def get_context_data(self, **kwargs):
        context = super(Menu, self).get_context_data(**kwargs)
        print("\nthis is menu model\n")
        return context
    
'''
الفسم المسؤل عن بناء صفحات المستخدمين

'''
class Add_user_page(CreateView):
    model = User
    form_class=Add_user_form
    template_name='registration/reg.html'
    #success_url='/'
    
    def get_context_data(self, **kwargs):
        context = super(Add_user_page, self).get_context_data(**kwargs)
        print("\nadding new user\n")
        print(f"\nview users:\n{str(User.objects.all())}\n")
        return context
    def is_valid(self):
        valid = super().is_valid()
        user_k=self.request.user.pk
        user_n=User.objects.last()
        login(self.request,user_n)
        if not valid:
            return False
        # Custom Logic
        
        print(f"\nUSER {user_k}-{user_n} CREATED AND SAVED BY YOURS\n")
        
        #return redirct('core:make_profile',kwargs={'user_k':user_k,'p_name':user_n})
        print(f'add_user/makeing_profile_for_{str(user_n.pk)}_{user_n.username}')
        #return f'add_user/makeing_profile_for_{user_k}_{user_n}'
        #return redirect('core:make_profile',kwargs={'user_k':user_k,'p_name':user_n})
        return True
    
    def get_success_url(self):
        user_n=User.objects.last()
        login(self.request,user_n)
        print(f"\nUSER {str(user_n.pk)}-{user_n.username} CREATED BY YOURS\n")
        
        #return redirct('core:make_profile',kwargs={'user_k':user_k,'p_name':user_n})
        #return f'add_user/makeing_profile_for_{str(user_n.pk)}_{user_n.username}'
        return reverse('core:make_profile',kwargs={'user_k':user_n.pk,'p_name':user_n.username})

    



class Make_profile_page(CreateView):
    model = User_profile_model
    form_class=Make_UserProfile_form
    template_name='dir_1/item_1.html'
    def get_context_data(self, **kwargs):
        context = super(Make_profile_page, self).get_context_data(**kwargs)
        print("\nadding new profile for user x\n")
        return context
    
    def form_valid(self, form: Make_UserProfile_form):
        user_x=self.request.user
        form.instance.owned_by=user_x if user_x else "NO DATA"
        print("\nLast details on user "+str(user_x)+"\n")
        return super(Make_profile_page,self).form_valid(form)


    def get_success_url(self):
        user_k=self.request.user.pk
        user_n=self.request.user.username
        
        return reverse('core:view_profile',kwargs={'user_k':user_k,'p_name':user_n})



class View_profile_page(TemplateView):
    template_name='dir_1/item_2.html'
    def get_context_data(self, **kwargs):
        context = super(View_profile_page, self).get_context_data(**kwargs)
        user_k=kwargs['user_k']
        user_n=kwargs['p_name']
        print(f"\n display profile of user {str(user_k)}-{user_n}\n")
        display_profiles=User_profile_model.objects.all()
        print(f"\n display user profiles:\n\n {display_profiles}\n")
        context['user_profile']=User_profile_model.objects.get(owned_by=self.request.user.pk)
        context['traders']=trader_zone
        context['trader_goods']=Goods_model.objects.filter(owned_by=self.request.user.pk)
        context['restaurants']=Restaurant_model.objects.filter(owned_by=self.request.user.pk)
        context['companys_ser']=Service_provider_model.objects.filter(owned_by=self.request.user.pk)
        context['services']=Service_model.objects.filter(owned_by=self.request.user.pk)
        context['providors']=User_profile_model.objects.filter(owned_by=self.request.user.pk)

        user_profile_host=self.request.get_host()
        print(f"\n the URL:{str(user_profile_host)}\n")


       
        return context
    
    def get_success_url(self):pass


#dir_2:the trader activity

class Add_trade_activity_page(CreateView):
    model = Trader_model
    form_class=Trader_activity_form
    template_name='dir_2/item_1.html'
    def get_context_data(self, **kwargs):
        context = super(Add_trade_activity_page, self).get_context_data(**kwargs)
        print(f"add a trade activity model for user x")
        return context
    

    def form_valid(self, form: Trader_activity_form):
        user_x=self.request.user
        form.instance.owned_by=user_x if user_x else "NO DATA"
        print("\nLast details on user "+str(user_x)+"\n")
        return super(Add_trade_activity_page,self).form_valid(form)
    
    def get_success_url(self):
        user_n=self.request.user.username
        user_k=self.request.user.pk
        
        #return redirct('core:make_profile',kwargs={'user_k':user_k,'p_name':user_n})
        #return f'add_user/makeing_profile_for_{str(user_n.pk)}_{user_n.username}'
        return reverse('core:view_profile',kwargs={'user_k':user_k,'p_name':user_n})
    
class Update_trade_activity_page(UpdateView):
    model = Trader_model
    form_class=Trader_activity_form
    template_name='dir_2/item_1.html'
    pk_url_kwarg ='key'
    def get_success_url(self):
        user_n=self.request.user.username
        user_k=self.request.user.pk
        
        #return redirct('core:make_profile',kwargs={'user_k':user_k,'p_name':user_n})
        #return f'add_user/makeing_profile_for_{str(user_n.pk)}_{user_n.username}'
        return reverse('core:view_profile',kwargs={'user_k':user_k,'p_name':user_n})

class View_trade_activity_page(TemplateView):
    template_name='dir_2/item_3.html'
    def get_context_data(self, **kwargs):
        context = super(View_trade_activity_page, self).get_context_data(**kwargs)
        context['user_x']=User_profile_model.objects.get(owned_by=self.request.user.pk)
        
        context['items']=Trader_model.objects.filter(owned_by=self.request.user.pk)
        print(f"display the trade activity of {self.request.user.username}")
        return context


def trade_model(h,p_name,user_k,key):
    return render(h,'dir_2/view_item.html',{})



#dir_3:goods of the trader
class Add_goods_page(CreateView):
    model = Goods_model
    form_class=Add_a_Goods_model_form
    template_name='dir_3/item_1.html'
    def get_context_data(self, **kwargs):
        context = super(Add_goods_page, self).get_context_data(**kwargs)
        print(f"add a trade activity model for user x")
        return context
    

    def form_valid(self, form: Add_a_Goods_model_form):
        user_x=self.request.user
        form.instance.owned_by=user_x if user_x else "NO DATA"
        print("\nLast details on user "+str(user_x)+"\n")
        return super(Add_goods_page,self).form_valid(form)
    
    def get_success_url(self):
        user_n=self.request.user.username
        user_k=self.request.user.pk
        
        #return redirct('core:make_profile',kwargs={'user_k':user_k,'p_name':user_n})
        #return f'add_user/makeing_profile_for_{str(user_n.pk)}_{user_n.username}'
        return reverse('core:view_profile',kwargs={'user_k':user_k,'p_name':user_n})
    
class Update_goods_page(UpdateView):
    model = Goods_model
    form_class=Add_a_Goods_model_form
    template_name='dir_3/item_1.html'
    pk_url_kwarg='key'
    def get_success_url(self):
        user_n=self.request.user.username
        user_k=self.request.user.pk
        
        #return redirct('core:make_profile',kwargs={'user_k':user_k,'p_name':user_n})
        #return f'add_user/makeing_profile_for_{str(user_n.pk)}_{user_n.username}'
        return reverse('core:view_profile',kwargs={'user_k':user_k,'p_name':user_n})

class View_trader_goods_page(TemplateView):
    template_name='dir_3/item_3.html'
    def get_context_data(self, **kwargs):
        context = super(View_trader_goods_page, self).get_context_data(**kwargs)
        context['items']=Goods_model.objects.filter(owned_by=self.request.user.pk)
        print(f"display the trade activity of {self.request.user.username}")
        print(f"the url :{str(HttpRequest.body)}")
        print(f"all products of {str(self.request.user.username)} :\ncounts:{str(Goods_model.objects.filter(owned_by=self.request.user.pk).count)}")
        
        return context

def view_goods_item(h,p_name,user_k,key):
    the_host=h.get_host()
    print(f"\n\nthe host of {the_host}\n\n")

    item=Goods_model.objects.get(pk=key)
    view_payment_det=make_a_checkout(PAYPAL_RECIVER_EMAIL,
                                     item.price_after_discount(),
                                     item.name,u_pay_key.uuid4(),'EGP',
                                     f"http://{the_host}{reverse('paypal-ipn')}",
                                     f"http://{the_host}/win",
                                     f"http://{the_host}/fail",)
    payment_permission=PayPalPaymentsForm(initial=view_payment_det)
    
    '''auth=('rzp_test_wJF0LqMwPUIsda','M6CvoyyI3WJQzP4sY4az3S6s')
    if h.method == 'POST':
        get_Razorpay_data(5000,'EGP',razorpay.Client(auth))'''
    
    return render(h,'dir_3/view_item.html',{'item_x':item,'form':payment_permission,'key':STRIPE_PUBLISHABLE_KEY})

def win_case(h):
    user_n=h.user.username
    user_k=h.user.pk
    print(f"win case for client")
    reverse('core:view_profile',kwargs={'user_k':user_k,'p_name':user_n})

def win_case2(h,item_x):
    user_n=h.user.username
    user_k=h.user.pk
    item=Goods_model.objects.get(pk=item_x)
    if h.method == 'POST':
        client_order=stripe.Charge.create(amount=item.price_after_discount(),currency='EGP',description=item.name,source=h.POST['stripeToken'])
        print(f"\nPAYMENT OPERATION SUCCESS\n{client_order}\n")
    
    print(f"win case for client")
    reverse('core:view_profile',kwargs={'user_k':user_k,'p_name':user_n})



def fail_case(h):
    user_n=h.user.username
    user_k=h.user.pk
    print(f"fall case for client")
    reverse('core:view_profile',kwargs={'user_k':user_k,'p_name':user_n})

def remove_goods_item(h,p_name,user_k,key):
   the_host=h.get_host()
   try:  
    call=Goods_model.objects.get(pk=key)
    call.delete()
    print("\n\na product item was destroyed\n\n")
    return HttpResponsePermanentRedirect(f"http://{the_host}/profile_model_of_{str(user_k)}_{p_name}")
    #return redirect(f"profile_model_of_<int:user_k>_<str:p_name>")
        
   except AttributeError:pass
       



#dir_4:Service_provider_type
class Add_Service_provider_page(CreateView):
    model = Service_provider_model
    form_class=Add_Service_company_model
    template_name='dir_4/item_1.html'
    def get_context_data(self, **kwargs):
        context = super(Add_Service_provider_page, self).get_context_data(**kwargs)
        print(f"add a trade activity model for user x")
        return context
    

    def form_valid(self, form: Add_Service_company_model):
        user_x=self.request.user
        form.instance.owned_by=user_x if user_x else "NO DATA"
        print("\nLast details on user "+str(user_x)+"\n")
        return super(Add_Service_provider_page,self).form_valid(form)
    
    def get_success_url(self):
        user_n=self.request.user.username
        user_k=self.request.user.pk
        
        #return redirct('core:make_profile',kwargs={'user_k':user_k,'p_name':user_n})
        #return f'add_user/makeing_profile_for_{str(user_n.pk)}_{user_n.username}'
        return reverse('core:view_profile',kwargs={'user_k':user_k,'p_name':user_n})
    
class Update_Service_provider_page(UpdateView):
    model = Service_provider_model
    form_class=Add_Service_company_model
    template_name='dir_4/item_1.html'
    pk_url_kwarg='key'
    def get_success_url(self):
        user_n=self.request.user.username
        user_k=self.request.user.pk
        
        #return redirct('core:make_profile',kwargs={'user_k':user_k,'p_name':user_n})
        #return f'add_user/makeing_profile_for_{str(user_n.pk)}_{user_n.username}'
        return reverse('core:view_profile',kwargs={'user_k':user_k,'p_name':user_n})

class View_Service_provider_page(TemplateView):
    
    template_name='dir_4/item_3.html'
    def get_context_data(self, **kwargs):
        context = super(View_Service_provider_page, self).get_context_data(**kwargs)
        context['items']=Service_provider_model.objects.filter(owned_by=self.request.user.pk)
        print(f"display the company items of {self.request.user.username}")
        return context


def service_provider_item(h,p_name,user_k,key):
    return render(h,'dir_4/view_item.html',{})


#dir_5:Model of service
class Add_service_model_page(CreateView):
    model = Service_model
    form_class=Add_Service_model
    template_name='dir_5/item_1.html'
    def get_context_data(self, **kwargs):
        context = super(Add_service_model_page, self).get_context_data(**kwargs)
        print(f"add a trade activity model for user x")
        return context
    

    def form_valid(self, form: Add_Service_model):
        user_x=self.request.user
        form.instance.owned_by=user_x if user_x else "NO DATA"
        print("\nLast details on user "+str(user_x)+"\n")
        return super(Add_service_model_page,self).form_valid(form)
    
    def get_success_url(self):
        user_n=self.request.user.username
        user_k=self.request.user.pk
        
        #return redirct('core:make_profile',kwargs={'user_k':user_k,'p_name':user_n})
        #return f'add_user/makeing_profile_for_{str(user_n.pk)}_{user_n.username}'
        return reverse('core:view_profile',kwargs={'user_k':user_k,'p_name':user_n})
    
class Update_service_model_page(UpdateView):
    model = Service_model
    form_class=Add_Service_model
    template_name='dir_5/item_1.html'
    pk_url_kwarg='key'
    def get_success_url(self):
        user_n=self.request.user.username
        user_k=self.request.user.pk
        
        #return redirct('core:make_profile',kwargs={'user_k':user_k,'p_name':user_n})
        #return f'add_user/makeing_profile_for_{str(user_n.pk)}_{user_n.username}'
        return reverse('core:view_profile',kwargs={'user_k':user_k,'p_name':user_n})

class View_service_model_page(TemplateView):
    
    template_name='dir_5/item_3.html'
    def get_context_data(self, **kwargs):
        context = super(View_Service_provider_page, self).get_context_data(**kwargs)
        context['items']=Service_model.objects.filter(owned_by=self.request.user.pk)
        print(f"display the services of {self.request.user.username}")
        return context


def service_item(h,p_name,user_k,key):
    return render(h,'dir_5/view_item.html',{})



#dir_6:restaurant_model
class Add_restaurant_page(CreateView):
    model = Restaurant_model
    form_class=Add_restaurant_model
    template_name='dir_6/item_1.html'
    def get_context_data(self, **kwargs):
        context = super(Add_restaurant_page, self).get_context_data(**kwargs)
        print(f"add a trade activity model for user x")
        return context
    

    def form_valid(self, form: Add_a_Goods_model_form):
        user_x=self.request.user
        form.instance.owned_by=user_x if user_x else "NO DATA"
        print("\nLast details on user "+str(user_x)+"\n")
        return super(Add_restaurant_page,self).form_valid(form)
    
    def get_success_url(self):
        user_n=self.request.user.username
        user_k=self.request.user.pk
        
        #return redirct('core:make_profile',kwargs={'user_k':user_k,'p_name':user_n})
        #return f'add_user/makeing_profile_for_{str(user_n.pk)}_{user_n.username}'
        return reverse('core:view_profile',kwargs={'user_k':user_k,'p_name':user_n})
    
class Update_restaurant_page(UpdateView):
    model = Restaurant_model
    form_class=Add_restaurant_model
    template_name='dir_6/item_1.html'
    pk_url_kwarg='key'
    def get_success_url(self):
        user_n=self.request.user.username
        user_k=self.request.user.pk
        
        #return redirct('core:make_profile',kwargs={'user_k':user_k,'p_name':user_n})
        #return f'add_user/makeing_profile_for_{str(user_n.pk)}_{user_n.username}'
        return reverse('core:view_profile',kwargs={'user_k':user_k,'p_name':user_n})

class View_restaurant_page(TemplateView):
    template_name='dir_6/item_3.html'
    def get_context_data(self, **kwargs):
        context = super(View_restaurant_page, self).get_context_data(**kwargs)
        user_n=self.kwargs['p_name']
        user_k=self.kwargs['user_k']
        print(f"displaying all restaurant branches of {str(user_k)}-{user_n}")
        context['items']=Restaurant_model.objects.filter(owned_by=self.request.user.pk)
        return context

def res_item(h,p_name,user_k,key):
    return render(h,'dir_6/view_item.html',{})
    