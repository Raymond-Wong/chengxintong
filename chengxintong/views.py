# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
reload(sys)
sys.setdefaultencoding('utf-8')

from django.http import HttpResponse, HttpRequest, HttpResponseServerError, Http404
from django.shortcuts import render_to_response, redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

def welcome(request):
  return render_to_response('welcome.html')

def login(request):
  return render_to_response('login.html')

def regist(request):
  return render_to_response('regist.html')

def find_password(request):
  return render_to_response('find_password.html')

def home(request):
  return render_to_response('home.html')

def health(request):
  return render_to_response('health.html')

def career(request):
  return render_to_response('career.html')

def treasure(request):
  return render_to_response('treasure.html')

def app_list(request):
  return render_to_response('app_list.html')

