from __future__ import unicode_literals

from django.db import models
from dbarray import IntegerArrayField


class Company(models.Model):
	name = models.CharField(max_length=50)
	earnings = models.IntegerField(blank=True, null=True)
	path = IntegerArrayField(blank=True, editable=False)
	depth = models.PositiveSmallIntegerField(default=0)

	def __unicode__(self):
		return self.name