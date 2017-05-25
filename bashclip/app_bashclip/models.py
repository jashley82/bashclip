# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Command(models.Model):
    cmd_text = models.CharField(max_length=200)
    base_cmd = models.CharField(max_length=200)
    flags = models.CharField(max_length=200)
    args = models.CharField(max_length=200)
    line_no = models.IntegerField(default=0)

    def __str__(self):
        return self.base_cmd

    def save(self, *args, **kwargs):
        # TODO: Parse base_cmd, flags, and args
        super(Command, self).save(*args, **kwargs)
