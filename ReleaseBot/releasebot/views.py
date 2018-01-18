# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Releases
from .models import Products
from .models import ProductReleases
from .models import Accounts
from .models import AccountReleases


# Create your views here.
def index(request):

    template = loader.get_template('releasebot/index.html')
    releases = Releases.objects.all().filter(type="Official").order_by('-order')
    weeklys = Releases.objects.all().filter(type="Weekly").order_by('-order')
    products = Products.objects.all().order_by('-order')
    allReleases = ProductReleases.objects.all()
    #result = []
    #for productRelease in allReleases:
    #    accountRelease = AccountReleases.objects.all().filter(id=productRelease.productId).get()
    #    account = Accounts.objects.all().filter(id=accountRelease).get()
    #    type('', (object,), {'account': account.name, 'b': 6, 'c': 7})()

    context = {
        'releases': releases,
        'weeklys': weeklys,
        'products': products,
  #      'builds': allReleases,
    }
    return HttpResponse(template.render(context, request))


def release(request, release_id):
    template = loader.get_template('releasebot/release.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def account(request, account_id, environment_id, product_id):
    template = loader.get_template('releasebot/account.html')
    table = []
    context = {
        'account': Accounts.objects.all().filter(id=account_id).get(),
        'environment': environment_id,
        'product': product_id,
        'table': table
    }
    return HttpResponse(template.render(context, request))

def publish_release(request):
    template = loader.get_template('releasebot/publish_release.html')
    context = {

    }
    return HttpResponse(template.render(context, request))

def success(request):
    template = loader.get_template('releasebot/success.html')
    context = {

    }
    return HttpResponse(template.render(context, request))
