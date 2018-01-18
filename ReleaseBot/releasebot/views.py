# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Releases
from .models import Products
from .models import ProductReleases


# Create your views here.
def index(request):
    template = loader.get_template('releasebot/index.html')
    releases = Releases.objects.all().filter(type="Official").order_by('-order')
    weeklys = Releases.objects.all().filter(type="Weekly").order_by('-order')
    products = Products.objects.all().order_by('-order')
    allReleases = Releases.objects.all()

    context = {
        'releases': releases,
        'weeklys': weeklys,
        'products': products,
        'builds': allReleases,
    }
    return HttpResponse(template.render(context, request))


def release(request, release_id):
    template = loader.get_template('releasebot/release.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def account(request, account_id):
    template = loader.get_template('releasebot/account.html')
    context = {

    }
    return HttpResponse(template.render(context, request))
