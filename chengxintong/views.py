# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
reload(sys)
sys.setdefaultencoding('utf-8')
import json
import random
import string

from django.http import HttpResponse, HttpRequest, HttpResponseServerError, Http404
from django.shortcuts import render, redirect, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.utils import timezone
from datetime import date, timedelta

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
    params.append(dict(errno=0, identify=123, error="登陆成功"))
    params.append(dict(errno=1, identify=123, error="用户名或密码错误"))
    return HttpResponse(json.dumps(random.choice(params)), content_type="application/json")
  return render_to_response('login.html')

'''
注册页
'''
@csrf_exempt
def regist(request):
  if request.method == 'POST':
    params = []
    params.append(dict(errno=0, error="注册成功"))
    params.append(dict(errno=1, error="手机号已注册"))
    return HttpResponse(json.dumps(random.choice(params)), content_type="application/json")
  return render_to_response('regist.html')

'''
获取验证码
'''
@csrf_exempt
def verify(request):
  if request.method == 'POST':
    params = []
    params.append(dict(errno=0, error="注册成功"))
    params.append(dict(errno=1, error="请求超时，请稍后再试"))
    return HttpResponse(json.dumps(random.choice(params)), content_type="application/json")

'''
找回密码页
'''
@csrf_exempt
def find_password(request):
  if request.method == 'POST':
    params = []
    params.append(dict(errno=0, error="重置成功"))
    params.append(dict(errno=1, error="请求超时，请稍后再试"))
    return HttpResponse(json.dumps(random.choice(params)), content_type="application/json")
  return render_to_response('find_password.html')

'''
首页
'''
def home(request):
  return render_to_response('home.html')

'''
获取幻灯片列表
'''
@csrf_exempt
def get_banner_list(request):
  banner = []
  banner.append(dict(name='slide1', image='http://www.runoob.com/wp-content/uploads/2014/07/slide1.png', url='http://www.baidu.com'))
  banner.append(dict(name='slide2', image='http://www.runoob.com/wp-content/uploads/2014/07/slide2.png', url='http://www.sina.com'))
  banner.append(dict(name='slide3', image='http://www.runoob.com/wp-content/uploads/2014/07/slide3.png'))
  params = dict(banner=banner, errno=0)
  return HttpResponse(json.dumps(params), content_type='application/json')

'''
获取未读消息数量
'''
@csrf_exempt
def get_msg_count(request):
  params = []
  params.append(dict(errno=0, count=5))
  params.append(dict(errno=0, count=0))
  # params.append(dict(errno=0, error="无效操作"))
  return HttpResponse(json.dumps(random.choice(params)), content_type='application/json')

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
@csrf_exempt
def family_account_detail(request):
  if request.method == 'POST':
    params = dict(errno=0)
    year = request.POST.get('year')
    month = request.POST.get('month')
    items = []
    diff = 0.5
    if int(request.POST.get('type')) == 1:
      diff = 0
    elif int(request.POST.get('type')) == 2:
      diff = 1
    for i in xrange(10):
      items.append(dict(name="".join(random.sample(string.letters, random.randint(1, 10))), money=(random.random() - diff) * 1000, balance=random.random() * 10000, time="%s-%s-10" % (year, month)))
    params['list'] = items
    return HttpResponse(json.dumps(params), content_type='application/json')
  return render_to_response('family_account_detail.html')

'''
家庭账号余额页
'''
def family_account_balance(request):
  return render_to_response('family_account_balance.html')

'''
个人账户明细页
'''
@csrf_exempt
def user_account_detail(request):
  if request.method == 'POST':
    params = dict(errno=0)
    year = request.POST.get('year')
    month = request.POST.get('month')
    items = []
    diff = 0.5
    if int(request.POST.get('type')) == 1:
      diff = 0
    elif int(request.POST.get('type')) == 2:
      diff = 1
    for i in xrange(10):
      items.append(dict(name="".join(random.sample(string.letters, random.randint(1, 10))), money=(random.random() - diff) * 1000, balance=random.random() * 10000, time="%s-%s-10" % (year, month)))
    params['list'] = items
    return HttpResponse(json.dumps(params), content_type='application/json')
  return render_to_response('user_account_detail.html')

'''
个人账户
'''
def user_account(request):
  return render_to_response('user_account.html')

'''
签到页
'''
@csrf_exempt
def clock_in(request):
  if request.method == 'POST':
    params = dict(errno=0, money=100, message="签到成功")
    return HttpResponse(json.dumps(params), content_type="application/json")
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

'''
获取用户信息接口
'''
@csrf_exempt
def get_user_info_data(request):
  params = [dict(errno=0, error="系统升级中，请求失败")]
  params = []
  sign_goon = random.randint(0, 200)
  params.append(dict(sign_state=random.choice([0, 1]), sign_nums=random.randint(0, 1000), sign_goon=sign_goon, sign_days=random.randint(sign_goon, sign_goon + 100), family_yestoday=random.random() * 1000, family_today=random.random() * 1000, family_planning=random.random() * 100000, family_money=random.randint(0, 10000), personal_money=random.randint(0, 10000), personal_today=random.randint(0, 1000), sign_money=random.random() * 10))
  return HttpResponse(json.dumps(random.choice(params)), content_type="application/json")

'''
获取用户签到日期
'''
@csrf_exempt
def get_sign_in_days(request):
  year = int(request.POST.get('year'))
  month = int(request.POST.get('month'))
  fdm = date(year, month, 1)
  cd = date(fdm.year, fdm.month, fdm.day)
  dates = []
  while cd.month == fdm.month:
    dates.append(cd.day)
    cd += timedelta(days=1)
  params = dict(errno=0, list=random.sample(dates, random.randint(5, len(dates))))
  return HttpResponse(json.dumps(params), content_type='application/json')
