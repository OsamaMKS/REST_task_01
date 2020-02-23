from .models import Flight, Booking
from rest_framework.generics import ListAPIView
from django.shortcuts import render
from datetime import datetime

from .serializers import FligthSerializer, BookingSerializer

class FlightsList(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FligthSerializer

class BookingList(ListAPIView):
    queryset = Booking.objects.filter(date__gt=datetime.today())
    serializer_class = BookingSerializer
