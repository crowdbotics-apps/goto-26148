from rest_framework import authentication
from delivery_order.models import Order, PaymentMethod, Bill
from .serializers import OrderSerializer, PaymentMethodSerializer, BillSerializer
from rest_framework import viewsets


class BillViewSet(viewsets.ModelViewSet):
    serializer_class = BillSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Bill.objects.all()


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Order.objects.all()


class PaymentMethodViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentMethodSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = PaymentMethod.objects.all()
