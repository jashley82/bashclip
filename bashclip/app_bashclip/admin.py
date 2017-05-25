# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from app_bashclip.models import Command


@admin.register(Command)
class CommandAdmin(admin.ModelAdmin):
    pass
