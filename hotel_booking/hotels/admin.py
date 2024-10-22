from django.contrib import admin
from .models import *


admin.site.register(UserProfile)
admin.site.register(Hotel)
admin.site.register(HotelPhotos)
admin.site.register(Room)
admin.site.register(RoomPhotos)
admin.site.register(Review)
