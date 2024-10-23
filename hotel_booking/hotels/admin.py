from django.contrib import admin
from .models import *


class RoomPhotosInline(admin.TabularInline):
    model = RoomPhotos
    extra = 1


class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomPhotosInline]


admin.site.register(Room, RoomAdmin)

admin.site.register(UserProfile)
admin.site.register(Hotel)
admin.site.register(HotelPhotos)
admin.site.register(Review)
admin.site.register(Booking)
