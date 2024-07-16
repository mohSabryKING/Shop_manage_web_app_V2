from django.urls import path, re_path
from django.contrib.auth import views as auth_model
from .views import *

app_name = "core"

urlpatterns = [
      path('login',auth_model.LoginView.as_view(template_name="registration/login.html"),name='login'),
      path('logout',auth_model.LogoutView.as_view(template_name="registration/logout.html"),name='logout'),
      path('add_user',Add_user_page.as_view(),name='add_user'),
      path('add_user/makeing_profile_for_<int:user_k>_<str:p_name>',Make_profile_page.as_view(),name='make_profile'),
      path('profile_model_of_<int:user_k>_<str:p_name>',View_profile_page.as_view(),name='view_profile'),
      #trader_phase
      path('profile_model_of_<int:user_k>_<str:p_name>/add_trade_activity',Add_trade_activity_page.as_view(),name='add_trade_activity'),
      path('profile_model_of_<int:user_k>_<str:p_name>/view_trade_activity',View_trade_activity_page.as_view(),name='view_trade_activity'),
      path('profile_model_of_<int:user_k>_<str:p_name>/view_trade_activity/item_<int:key>/update',Update_trade_activity_page.as_view(),name='update_trade_activity'),
      path('profile_model_of_<int:user_k>_<str:p_name>/view_trade_activity/item_<int:key>/view',trade_model,name='view_trade_activity_item'),
      
      #add a goods model
      path('profile_model_of_<int:user_k>_<str:p_name>/add_product_model',Add_goods_page.as_view(),name='add_product_model'),
      path('profile_model_of_<int:user_k>_<str:p_name>/view_product_model',View_trader_goods_page.as_view(),name='view_product_model'),
      path('profile_model_of_<int:user_k>_<str:p_name>/view_product_model/item_<int:key>/update',Update_goods_page.as_view(),name='update_product_model'),
      path('profile_model_of_<int:user_k>_<str:p_name>/view_product_model/item_<int:key>/view',view_goods_item,name='view_item_product'),
      path('profile_model_of_<int:user_k>_<str:p_name>/view_product_model/item_<int:key>/kill',remove_goods_item,name='remove_item_product'),
      
      #add a Service provider data
      path('profile_model_of_<int:user_k>_<str:p_name>/add_Service_provider_model',Add_Service_provider_page.as_view(),name='add_service_provider_model'),
      path('profile_model_of_<int:user_k>_<str:p_name>/view_Service_provider_model',View_Service_provider_page.as_view(),name='view_service_provider_model'),
      path('profile_model_of_<int:user_k>_<str:p_name>/view_Service_provider_model/item_<int:key>/update',Update_Service_provider_page.as_view(),name='update_service_provider_model'),
      path('profile_model_of_<int:user_k>_<str:p_name>/view_Service_provider_model/item_<int:key>/view',service_provider_item,name='view_service_provider_item_model'),
      
      #add a Service model
      path('profile_model_of_<int:user_k>_<str:p_name>/add_service_model_model',Add_service_model_page.as_view(),name='add_service_model'),
      path('profile_model_of_<int:user_k>_<str:p_name>/view_service_model_model',View_service_model_page.as_view(),name='view_service_model'),
      path('profile_model_of_<int:user_k>_<str:p_name>/view_service_model_model/item_<int:key>/update',Update_service_model_page.as_view(),name='update_service_model'),
      path('profile_model_of_<int:user_k>_<str:p_name>/view_service_model_model/item_<int:key>/view',service_item,name='view_service_item_model'),
      
      #add a restaurant
      path('profile_model_of_<int:user_k>_<str:p_name>/add_restaurant_model',Add_restaurant_page.as_view(),name='add_restaurant_model'),
      path('profile_model_of_<int:user_k>_<str:p_name>/view_restaurant_model',View_restaurant_page.as_view(),name='view_restaurant_model'),
      path('profile_model_of_<int:user_k>_<str:p_name>/view_restaurant_model/item_<int:key>/update',Update_restaurant_page.as_view(),name='update_restaurant_model'),
      path('profile_model_of_<int:user_k>_<str:p_name>/view_restaurant_model/item_<int:key>/view',res_item,name='virw_restaurant_item_model'),
      



      path('profile_model_of_<int:user_k>_<str:p_name>',View_profile_page.as_view(),name='view_profile'),
      
      path('',Menu.as_view(),name='home'),
      path('win',win_case,name='win'),
      path('win2_for_item_<int:item_x>',win_case2,name='win2'),
      path('fail',fail_case,name='fail'),
    
]