from __future__ import unicode_literals

from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=40, blank=True, null=True)
    last_name = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        ordering = ('last_name',)

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name


class Invoice(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    project_title = models.CharField(max_length=100)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='invoices')

    class Meta:
        ordering = ('created',)

    def __unicode__(self):
        return self.project_title


class LineItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='lineitems')
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=200, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.PositiveIntegerField(null=True)

    def __unicode__(self):
        return self.name
