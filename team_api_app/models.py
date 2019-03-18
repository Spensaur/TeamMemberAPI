# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class TeamMember(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	phone_number = models.BigIntegerField()
	email = models.EmailField()
	admin_role = models.BooleanField(default=False)

	def __str__(self):
		return (
				self.first_name + ' ' + self.last_name + '\n' +
				str(self.phone_number) + '\n' +
				str(self.email) + '\n' +
				'admin: ' + str(self.admin_role)
		)
