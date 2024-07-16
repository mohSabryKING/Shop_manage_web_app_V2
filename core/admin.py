from typing import Any
from django.contrib import admin
from django.db.models.fields.related import ForeignKey
from django.db.models.query import QuerySet
from django.forms.models import ModelChoiceField
from django.http.request import HttpRequest
from django.utils.html import *
from .models import *
from django import forms
from import_export.admin import ImportExportModelAdmin
# Register your models here.



admin.site.login_template='registration/login.html'
admin.site.logout_template='registration/logout.html'





class Csv_trader_model(ImportExportModelAdmin):pass

class Csv_Users_model(ImportExportModelAdmin):pass

class Csv_service_items(ImportExportModelAdmin):pass

class Csv_service_provider_model(ImportExportModelAdmin):pass

class Csv_red_model(ImportExportModelAdmin):pass

class Csv_goods_model(ImportExportModelAdmin):pass




class Helper_user(admin.ModelAdmin):
      def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
            q=super().get_queryset(request)
            if request.user.is_superuser :
                  print(f"\na query of {request.user} was found Helper_user\n")
                  return q
            print(f"a profile owned by {request.user} Helper_user")
            return q.filter(owned_by=request.user)
class Helper_service_provider(admin.ModelAdmin):
      fields = ('owned_by','company_name','img_logo','address','branch_locat')
        
      def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
            q=super().get_queryset(request)
            if request.user.is_superuser :
                  print(f"\na query of {request.user} was found Helper_service_provider\n")
                  return q
            print(f"a profile owned by {request.user} Helper_service_provider")
            return q.filter(owned_by=request.user)
class Helper_service_model(admin.ModelAdmin):
      fields = ('owned_by','provider','name','img_serve','price','des')
       
      def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
            q=super().get_queryset(request)
            if request.user.is_superuser :
                  print(f"\na query of {request.user} was found Helper_service_model\n")
                  return q
            print(f"a profile owned by {request.user} Helper_service_model")
            return q.filter(owned_by=request.user)
class Helper_trader_model(admin.ModelAdmin):
      
      fields = ('t_name','address','branch_locat','des')
      def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
            q=super().get_queryset(request)
            if request.user.is_superuser :
                  print(f"\na query of {request.user} was found Helper_trader_model\n")
                  return q
            print(f"a profile owned by {request.user} Helper_trader_model")
            return q.filter(owned_by=request.user)
class Helper_restaurant(admin.ModelAdmin):
      
      fields = ('owned_by','r_name','img_locat','address','branch_locat','des')
      def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
            q=super().get_queryset(request)
            if request.user.is_superuser :
                  print(f"\na query of {request.user} was found Helper_trader_model\n")
                  return q
            print(f"a profile owned by {request.user} Helper_trader_model")
            return q.filter(owned_by=request.user)
class Helper_goods(admin.ModelAdmin):
      list_display=('btn_act_1','avil_func','product_photo','price_after_discount')
      
      fields = ('name','img_prod','des','discount_precent','price','amount','always_avil')
      def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
            q=super().get_queryset(request)
            if request.user.is_superuser :
                  print(f"\na query of {request.user} was found Helper_goods\n")
                  return q
            print(f"a profile owned by {request.user} Helper_goods")
            return q.filter(owned_by=request.user)
      def formfield_for_foreignkey(self, db_field: ForeignKey[Any], request: HttpRequest | None, **kwargs: Any) -> ModelChoiceField | None:
            return super().formfield_for_foreignkey(db_field, request, **kwargs)










admin.site.register(User_profile_model)
admin.site.register(Trader_model)
#admin.site.register(Goods_model,Helper_goods)





'''class Add_a_Goods_model_form(forms.BaseModelFormSet):
    #'owned_by','name','p_type','img_prod','des','discount_precent','amount','price_after_discount'
      
    class Meta:
        model = Goods_model
        fields = ('name','img_prod','des','discount_precent','price','amount','always_avil')
        widgets={'owned_by':forms.HiddenInput()}



'''




@admin.register(Goods_model)
class Csv_goods_model(ImportExportModelAdmin,Helper_goods):
      list_display=('btn_act_1','avil_func','product_photo')
      def print_model_v1():
            return format_html('<h1>mohemd</h1>')

admin.site.register(Service_provider_model)
admin.site.register(Service_model)
admin.site.register(Restaurant_model)


