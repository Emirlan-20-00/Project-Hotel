from django_filters import FilterSet
from .models import Hotel


class HotelFilter(FilterSet):
    class Meta:
        model = Hotel
        fields = {
            'price': ['gt', 'lt'],
            'active': ['exact'],
        }