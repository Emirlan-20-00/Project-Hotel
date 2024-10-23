from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = 'first_name', 'last_name'


class HotelListSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    date = serializers.DateField(format='%d-%m-%Y')

    class Meta:
        model = Hotel
        fields = ['id', 'name_hotel', 'country', 'city', 'date', 'average_rating', 'price',]

    def get_average_rating(self, obj):
        return obj.get_average_rating()


class HotelSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    date = serializers.DateField(format='%d-%m-%Y')

    class Meta:
        model = Hotel
        fields = ['id', 'name_hotel', 'country', 'city', 'date', 'average_rating', 'price', 'description', 'owner',
                  'active', 'hotel_video', 'room',]

    def get_average_rating(self, obj):
        return obj.get_average_rating()


class HotelPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelPhotos
        fields = ['image']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class RoomPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomPhotos
        fields = ['image']


class ReviewSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format='%d-%m-%Y %H:%M')

    class Meta:
        model = Review
        fields = '__all__'


class HotelDetailSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    date = serializers.DateField(format='%d-%m-%Y')
    reviews = ReviewSerializer(many=True, read_only=True)
    hotel = HotelPhotosSerializer(many=True, read_only=True)
    room = RoomSerializer(many=True, read_only=True)
    owner = UserProfileSimpleSerializer()

    class Meta:
        model = Hotel
        fields = ['id', 'name_hotel', 'country', 'date',  'description', 'reviews', ' average_rating',
                  'address', 'city', 'active', 'owner', 'hotel_video', 'hotel', 'price']

    def get_average_rating(self, obj):
        return obj.get_average_rating()


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'room', 'user', 'start_date', 'end_date']

    def create(self, validated_data):
        return Booking.objects.create(**validated_data)

    def validate(self, data):
        if data['user'].is_staff:  # Проверка, что владелец отеля не может бронировать
            raise serializers.ValidationError("Hotel owners cannot book their own rooms.")
        return data

