# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=200)
    order = models.IntegerField(default=1)
    jenkinsContainer = models.CharField(max_length=200)


class Releases(models.Model):
    name = models.CharField(max_length=200)
    order = models.IntegerField(default=1)
    type = models.CharField(max_length=50)
    date = models.DateField('date released')
    releaseNotes = models.CharField(max_length=200)
    technicalNotes = models.CharField(max_length=200)


class ProductReleases(models.Model):
    releaseId = models.ForeignKey(Releases)
    productId = models.ForeignKey(Products)
    jenkinsJobName = models.CharField(max_length=200)
    buildNumber = models.IntegerField


class ServicePacks(models.Model):
    name = models.CharField(max_length=200)
    order = models.IntegerField(default=1)
    productReleaseId = models.ForeignKey(ProductReleases)
    buildNumber = models.IntegerField
    date = models.DateField('date installed')


class Accounts(models.Model):
    name = models.CharField(max_length=200)
    order = models.IntegerField(default=1)


class AccountReleases(models.Model):
    accountId = models.ForeignKey(Accounts)
    productReleaseId = models.ForeignKey(ProductReleases)
    target = models.CharField(max_length=50)
    date = models.DateField('date released')

class AccountReleaseServicePack(models.Model):
    accountReleaseId = models.ForeignKey(AccountReleases)
    servicePackId = models.ForeignKey(ServicePacks)
    date = models.DateField('date installed')
