from django.conf.urls import patterns, include, url
import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chengxintong.views.home', name='home'),
    # url(r'^chengxintong/', include('chengxintong.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^welcome/$', views.welcome, name="welcome"),
    url(r'^login/$', views.login, name="login"),
    url(r'^regist/$', views.regist, name="regist"),
    url(r'^verify/$', views.verify, name="verify"),
    url(r'^find_password/$', views.find_password, name="find_password"),
    url(r'^home/$', views.home, name="home"),
    url(r'^health/$', views.health, name="health"),
    url(r'^career/$', views.career, name="career"),
    url(r'^treasure/$', views.treasure, name="treasure"),
    url(r'^app_list/$', views.app_list, name="app_list"),
    url(r'^family_account_detail/$', views.family_account_detail, name="family_account_detail"),
    url(r'^family_account_balance/$', views.family_account_balance, name="family_account_balance"),
    url(r'^user_account_detail/$', views.user_account_detail, name="user_account_detail"),
    url(r'^user_account/$', views.user_account, name="user_account"),
    url(r'^clock_in/$', views.clock_in, name="clock_in"),
    url(r'^clock_in_income/$', views.clock_in_income, name="clock_in_income"),
    url(r'^user_center/$', views.user_center, name="user_center"),
    url(r'^info_center/$', views.info_center, name="info_center"),
    url(r'^user_info_center/$', views.user_info_center, name="user_info_center"),
    url(r'^change_password/$', views.change_password, name="change_password"),
    url(r'^about/$', views.about, name="about"),
    url(r'^feedback/$', views.feedback, name="feedback"),
    url(r'^clock_in/$', views.clock_in, name="clock_in"),
    url(r'^get_banner_list/$', views.get_banner_list, name="get_banner_list"),
    url(r'^get_msg_count/$', views.get_msg_count, name="get_msg_count"),
    url(r'^get_user_info_data/$', views.get_user_info_data, name="get_user_info_data"),
    url(r'^get_sign_in_days/$', views.get_sign_in_days, name="get_sign_in_days"),
)
