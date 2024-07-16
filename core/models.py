from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from math import *
from django.utils.html import *
# Create your models here.

User_type=[('تاجر','تاجر'),
           ('عميل','عميل'),
           ('صاحب مطعم','صاحب مطعم'),
           ('موزع خدمات','موزع خدمات'),
           ]


location_url="https://maps.app.goo.gl/PmEMNyF8A5xRhLzS7"


topic_model="""
Sequi repellendus culpa nulla facilis, deserunt ad optio ab neque explicabo perspiciatis libero, impedit facere ut laborum totam. Repudiandae possimus, sit fuga eaque ipsa in minima
                aut nihil debitis at pariatur odit corporis maxime illo, iste blanditiis
"""

class User_profile_model(models.Model):
      #owned_by,p_name,p_type,img_user,img_bkg,user_phone
      owned_by = models.OneToOneField(User,  blank=True, null=True,on_delete=models.CASCADE)
      p_name = models.CharField(max_length=20, blank=True, null=True,verbose_name='الاسم',default="مجهول")
      p_type = models.CharField(max_length=20, blank=True, null=True,verbose_name='نوع النشاط',choices=User_type,default=User_type[0])
      img_user = models.ImageField(upload_to="user_img", height_field=None, width_field=None,verbose_name='صوره المستخدم', max_length=100,default='media/user_icon.jpg')
      img_bkg = models.ImageField(upload_to="user_bkg", height_field=None, width_field=None, max_length=100,verbose_name='خلفبة المستخدم',default='media/bkg_1.jpg')
      user_phone=PhoneNumberField(blank=False,verbose_name='الهاتف',)
      

      
      

      def __str__(self):return str(self.owned_by)
      def wa_business_link(self):pass
      
      def edit_link(self):pass
      def edit_link(self):pass
      def location_link(self):pass

      class Meta:
            db_table = ''
            managed = True
            verbose_name = 'صفحات المستخدمين'
            verbose_name_plural = 'صفحات المستخدمين'









class Trader_model(models.Model):
      #'owned_by','t_name','address','branch_locat',des
      owned_by = models.ForeignKey(User,related_name='profile_of_1', on_delete=models.CASCADE,null=True,blank=True)
      t_name = models.CharField(max_length=20, blank=True, null=True,verbose_name='الاسم',default="مجهول")
      
      address = models.CharField(max_length=50, blank=True, null=True,verbose_name='العنوان',default="45ش المخال-مصر الجديدة")
      branch_locat = models.URLField(max_length = 200,default=location_url)
      des = models.TextField(verbose_name='وصف النشاط',max_length=300,default=topic_model)
      
      

      def __str__(self):
            pass

      class Meta:
            db_table = ''
            managed = True
            verbose_name = 'قسم التجار'
            verbose_name_plural = 'قسم التجار'


class Restaurant_model(models.Model):
      #'owned_by','r_name','img_locat,'address','branch_locat','des'
      owned_by = models.ForeignKey(User, blank=True, null=True,related_name='profile_of_2', on_delete=models.CASCADE)
      r_name = models.CharField(max_length=20, blank=True, null=True,verbose_name='الاسم',default="مجهول")
      address = models.CharField(max_length=50, blank=True, null=True,verbose_name='العنوان',default="45ش المخال-مصر الجديدة")
      img_locat = models.ImageField(upload_to="branch_bkg", height_field=None, width_field=None, max_length=100,verbose_name='صوره لمكان الفرع',default='media/bkg_1.jpg')
      branch_locat = models.URLField(max_length = 200,default=location_url)
      des = models.TextField(verbose_name='وصف الفرع',max_length=300,default=topic_model)
      
      

      def __str__(self):
            pass

      class Meta:
            db_table = ''
            managed = True
            verbose_name = 'قسم المطاعم'
            verbose_name_plural = 'قسم المطاعم'

class Service_provider_model(models.Model):
      #'owned_by','company_name','img_logo'و'address','branch_locat'
      owned_by = models.ForeignKey(User, blank=True, null=True,related_name='owned_by_x', on_delete=models.CASCADE)
      img_logo = models.ImageField(upload_to="company_img",blank=True, null=True, height_field=None, width_field=None,verbose_name='شعار الشركة', max_length=100)
     
      company_name = models.CharField(max_length=20, blank=True, null=True,verbose_name='الاسم',default="مجهول")
      address = models.CharField(max_length=50, blank=True, null=True,verbose_name='العنوان',default="45ش المخال-مصر الجديدة")

      branch_locat = models.URLField(max_length = 200,blank=True, null=True,verbose_name='الموقع',default=location_url)
      


      def __str__(self):
            pass

      class Meta:
            db_table = ''
            managed = True
            verbose_name = 'الشركات'
            verbose_name_plural = 'الشركات'



class Goods_model(models.Model):
      #'owned_by','name','p_type','img_prod','des','discount_precent','amount','price_after_discount'
      owned_by = models.ForeignKey(User, blank=True, null=True,related_name='profile_of_3', on_delete=models.CASCADE)
      
      name = models.CharField(max_length=30, blank=True, null=True,default="تودو كب كيك",verbose_name='أسم المنتج')
      img_prod = models.ImageField(upload_to="product_img", height_field=None, width_field=None,verbose_name='صوره المنتج', max_length=100)
      price = models.FloatField(default=220.50,verbose_name='السعر', blank=True, null=True,)
      discount_precent=models.IntegerField(default=50,verbose_name='نسبة الخصم',)
      amount=models.IntegerField(default=50,verbose_name='الكمية',)
      always_avil = models.BooleanField(verbose_name="هذا المنتج متاح دائما")
      
      
      des = models.TextField(verbose_name='وصف المنتج',max_length=300,default=topic_model)
      #<a href="/admin/core/goods_model/3/change/">old shoo magic</a>

      def __str__(self):
            return self.name
      def price_after_discount(self):
            return ceil(self.price-(self.price * (self.discount_precent/100)))
      def btn_act_1(self):
            return format_html(f"<a href='/admin/core/goods_model/{str(self.pk)}/change/' class='admin_btn_v1'>تعديل</a>")
      def product_photo(self):
            return format_html(f"<img class='view_prod' id='prod_{self.pk}' width='100px' heigh='100px' src='{self.img_prod.url}' />")
      
      def avil_func(self):
            if self.always_avil:
                  return "متاح"
            else:
                  return "غير متاح"

      class Meta:
            db_table = ''
            managed = True
            verbose_name = 'البضائع والمنتجات'
            verbose_name_plural = 'البضائع والمنتجات'



class Service_model(models.Model):
      #'owned_by','provider','name','img_serve','price','des'
      owned_by = models.ForeignKey(User, blank=True, null=True,related_name='profile_of_4', on_delete=models.CASCADE)
      provider = models.ForeignKey(Service_provider_model, blank=True, null=True,related_name='provider', on_delete=models.CASCADE)
      
      name = models.CharField(max_length=30, blank=True, null=True,default="web development",verbose_name='أسم الخدمة')
      img_serve = models.ImageField(upload_to="serve_img", height_field=None, width_field=None,verbose_name='صوره للخدمة', max_length=100)
      price = models.FloatField(default=220.50,verbose_name='السعر', blank=True, null=True,)
      des = models.TextField(verbose_name='وصف الخدمة',max_length=300,default=topic_model)
      
     

      def __str__(self):
            return self.name

      class Meta:
            db_table = ''
            managed = True
            verbose_name = 'نماذج الخدمات المتاحة'
            verbose_name_plural = 'نماذج الخدمات المتاحة'





service_provider_zone=User_profile_model.objects.filter(p_type='موزع خدمات')
restaurant_zone=User_profile_model.objects.filter(p_type='صاحب مطعم')
client_zone=User_profile_model.objects.filter(p_type='عميل')
trader_zone=User_profile_model.objects.filter(p_type='تاجر')



service_provider_zone_count=User_profile_model.objects.filter(p_type='موزع خدمات').count()
restaurant_zone_count=User_profile_model.objects.filter(p_type='صاحب مطعم').count()
client_zone_count=User_profile_model.objects.filter(p_type='عميل').count()
trader_zone_count=User_profile_model.objects.filter(p_type='تاجر').count()