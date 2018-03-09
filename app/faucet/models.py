'''
    Copyright (C) 2017 Gitcoin Core

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.

'''
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.postgres.fields import JSONField
from django.db import models

# Create your models here.
from economy.models import SuperModel


class FaucetRequestManager(models.Manager):
    def user(self, profile):
        return self.filter(github_username = profile)


class FaucetRequest(SuperModel):
    fulfilled = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    github_username = models.CharField(max_length=255, db_index=True)
    github_meta = JSONField()
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    comment = models.TextField(max_length=500, blank=True)
    comment_admin = models.TextField(max_length=500, blank=True)
    fulfill_date = models.DateTimeField(null=True, blank=True)

    objects = FaucetRequestManager()

    def __str__(self):
        return f"{self.github_username} / {self.created_on}"
