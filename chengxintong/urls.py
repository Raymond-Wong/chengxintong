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
    url(r'^find_password/$', views.find_password, name="find_password"),
    url(r'^home/$', views.home, name="home"),
    url(r'^health/$', views.health, name="health"),
    url(r'^career/$', views.career, name="career"),
    url(r'^treasure/$', views.treasure, name="treasure"),
    url(r'^app_list/$', views.app_list, name="app_list"),
    url(r'^family_account_detail/$', views.app_list, name="app_list"),
    url(r'^family_account_balance/$', views.app_list, name="app_list"),
    url(r'^user_account_detail/$', views.app_list, name="app_list"),
    url(r'^user_account/$', views.app_list, name="app_list"),
    url(r'^clock_in/$', views.app_list, name="app_list"),
    url(r'^clock_in_income/$', views.app_list, name="app_list"),
    url(r'^user_center/$', views.app_list, name="app_list"),
    url(r'^info_center/$', views.app_list, name="app_list"),
    url(r'^user_info_center/$', views.app_list, name="app_list"),
    url(r'^change_password/$', views.app_list, name="app_list"),
    url(r'^about/$', views.app_list, name="app_list"),
    url(r'^feedback/$', views.app_list, name="app_list"),
)
