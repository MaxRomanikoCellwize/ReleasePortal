# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader


# Create your views here.
def index(request):
    template = loader.get_template('releasebot/index.html')
    context = {

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
