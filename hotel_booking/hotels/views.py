from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import HotelFilter
from rest_framework.filters import SearchFilter, OrderingFilter


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class HotelListViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = HotelFilter
    search_fields = ['name_hotel']
    ordering_fields = ['price', 'date']


class HotelDetailViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class HotelPhotosViewSet(viewsets.ModelViewSet):
    queryset = HotelPhotos.objects.all()
    serializer_class = HotelPhotosSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomPhotosViewSet(viewsets.ModelViewSet):
    queryset = RoomPhotos.objects.all()
    serializer_class = RoomPhotosSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
