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
from .models import ServicePacks


# Create your views here.
def index(request):

    template = loader.get_template('releasebot/index.html')
    releases = Releases.objects.all().filter(type="Official").order_by('-order')
    weeklys = Releases.objects.all().filter(type="Weekly").order_by('-order')
    products = Products.objects.all().order_by('-order')
    accountReleases = AccountReleases.objects.all().order_by('-date')
    result = []
    seenAccounts = []
    for accountRelease in accountReleases:
        account = accountRelease.accountId
        productRelease = accountRelease.productReleaseId
        release = productRelease.releaseId
        if account.id not in seenAccounts:
            result.append({'accountName': account.name, 'accountId': account.id, 'releaseName': release.name, 'buildNumber': productRelease.buildNumber })
            seenAccounts.append(account.id)

    context = {
        'releases': releases,
        'weeklys': weeklys,
        'products': products,
        'builds': result,
    }
    return HttpResponse(template.render(context, request))


def release(request, release_id):
    template = loader.get_template('releasebot/release.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def account(request, account_id, environment_id, product_id):
    template = loader.get_template('releasebot/account.html')
    if environment_id=='1':
        accountReleases = AccountReleases.objects.all().filter(target='Production').order_by('-date')
    else:
        accountReleases = AccountReleases.objects.all().filter(target='Pre-Production').order_by('-date')
    table = []
    for accountRelease in accountReleases:
        productRelease = accountRelease.productReleaseId
        if str(productRelease.productId.id) == product_id:
            release = productRelease.releaseId
            servicePacks = ServicePacks.objects.all().filter(productReleaseId=productRelease.id).order_by('-order')
            if servicePacks.count() > 0:
                servicePack = servicePacks[:1].get()
                table.append({'releaseName': release.name, 'releaseDate': release.date, 'servicePackName': servicePack.name, 'servicePackDate': servicePack.date})
            else:
                table.append({'releaseName': release.name, 'releaseDate': release.date, 'servicePackName': '',
                              'servicePackDate': ''})
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
