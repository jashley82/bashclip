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
        return self.cmd_text

    def save(self, *args, **kwargs):
        # TODO: Parse base_cmd, flags, and args
        base_cmd = self.cmd_text.split(' ')[0]
        if 'sudo' in base_cmd:
            self.base_cmd = 'sudo ' + base_cmd.split(' ')[1]
        else:
            self.base_cmd = base_cmd
        # print(self.base_cmd, self.cmd_text)
        print('i am sane')
        super(Command, self).save(*args, **kwargs)
