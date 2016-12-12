from django.shortcuts import render
from invoices.models import Invoice
from invoices.serializers import * 
from rest_framework import generics


class InvoiceList(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InvoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class LineItemList(generics.ListCreateAPIView):
    queryset = LineItem.objects.all()
    serializer_class = LineItemSerializer


class LineItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LineItem.objects.all()
    serializer_class = LineItemSerializer


class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
