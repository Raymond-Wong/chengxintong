# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
reload(sys)
sys.setdefaultencoding('utf-8')

from django.shortcuts import render_to_response

'''
启动页
'''
def welcome(request):
  return render_to_response('welcome.html')

'''
登陆页
'''
def login(request):
  return render_to_response('login.html')

'''
注册页
'''
def regist(request):
  return render_to_response('regist.html')

'''
找回密码页
'''
def find_password(request):
  return render_to_response('find_password.html')

'''
首页
'''
def home(request):
  return render_to_response('home.html')

'''
健康页
'''
def health(request):
  return render_to_response('health.html')

'''
事业页
'''
def career(request):
  return render_to_response('career.html')

'''
财富页
'''
def treasure(request):
  return render_to_response('treasure.html')

'''
全部应用页
'''
def app_list(request):
  return render_to_response('app_list.html')

'''
家庭账号明细页
'''
def family_account_detail(request):
  return render_to_response('family_account_detail.html')

'''
家庭账号余额页
'''
def family_account_balance(request):
  return render_to_response('family_account_balance.html')

'''
个人账户明细页
'''
def user_account_detail(request):
  return render_to_response('user_account_detail.html')

'''
个人账户
'''
def user_account(request):
  return render_to_response('user_account.html')

'''
签到页
'''
def clock_in(request):
  return render_to_response('clock_in.html')

'''
签到收益
'''
def clock_in_income(request):
  return render_to_response('clock_in_income.html')

'''
个人中心
'''
def user_center(request):
  return render_to_response('user_center.html')

'''
消息中心
'''
def info_center(request):
  return render_to_response('info_center.html')

'''
用户中心
'''
def user_info_center(request):
  return render_to_response('user_info_center.html')

'''
修改密码
'''
def change_password(request):
  return render_to_response('change_password.html')

'''
关于
'''
def about(request):
  return render_to_response('about.html')

'''
意见反馈
'''
def feedback(request):
  return render_to_response('feedback.html')