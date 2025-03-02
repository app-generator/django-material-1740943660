# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    username = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Customer(models.Model):

    #__Customer_FIELDS__
    email = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    others = models.TextField(max_length=255, null=True, blank=True)

    #__Customer_FIELDS__END

    class Meta:
        verbose_name        = _("Customer")
        verbose_name_plural = _("Customer")


class Job(models.Model):

    #__Job_FIELDS__
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    appointment_id = models.CharField(max_length=255, null=True, blank=True)
    locale = models.CharField(max_length=255, null=True, blank=True)
    location_id = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    end_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    retry_interval = models.IntegerField(null=True, blank=True)
    send_announcement = models.BooleanField()
    interview_type = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    payment = models.BooleanField()
    amount = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    log = models.TextField(max_length=255, null=True, blank=True)
    others = models.TextField(max_length=255, null=True, blank=True)

    #__Job_FIELDS__END

    class Meta:
        verbose_name        = _("Job")
        verbose_name_plural = _("Job")



#__MODELS__END
