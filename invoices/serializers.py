from rest_framework import serializers
from invoices.models import Invoice, Client, LineItem
from django.contrib.auth.models import User

class InvoiceSerializer(serializers.ModelSerializer):
    #lineitems = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    client = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Invoice
        depth = 1
        fields = ('id', 'project_title','client','lineitems',)


class LineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineItem
        fields = ('id', 'name', 'description', 'price', 'quantity', 'invoice',)


class ClientSerializer(serializers.ModelSerializer):
    invoices = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ('id', 'first_name', 'last_name', 'invoices')
