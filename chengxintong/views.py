# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
reload(sys)
sys.setdefaultencoding('utf-8')
import json
import random

from django.http import HttpResponse, HttpRequest, HttpResponseServerError, Http404
from django.shortcuts import render, redirect, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.utils import timezone

'''
启动页
'''
def welcome(request):
  return render_to_response('welcome.html')

'''
登陆页
'''
@csrf_exempt
def login(request):
  if request.method == 'POST':
    params = []
    params.append(dict(errno=0, identify=123, msg="登陆成功"))
    params.append(dict(errno=1, identify=123, msg="用户名或密码错误"))
    return HttpResponse(json.dumps(random.choice(params)), content_type="application/json")
  return render_to_response('login.html')

'''
注册页
'''
@csrf_exempt
def regist(request):
  if request.method == 'POST':
    params = []
    params.append(dict(errno=0, msg="注册成功"))
    params.append(dict(errno=1, msg="手机号已注册"))
    return HttpResponse(json.dumps(random.choice(params)), content_type="application/json")
  return render_to_response('regist.html')

'''
获取验证码
'''
@csrf_exempt
def verify(request):
  if request.method == 'POST':
    params = []
    params.append(dict(errno=0, msg="注册成功"))
    params.append(dict(errno=1, msg="请求超时，请稍后再试"))
    return HttpResponse(json.dumps(random.choice(params)), content_type="application/json")

'''
找回密码页
'''
@csrf_exempt
def find_password(request):
  if request.method == 'POST':
    params = []
    params.append(dict(errno=0, msg="重置成功"))
    params.append(dict(errno=1, msg="请求超时，请稍后再试"))
    return HttpResponse(json.dumps(random.choice(params)), content_type="application/json")
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

'''
今日签到
'''
def feedback(request):
  return render_to_response('clock_in.html')