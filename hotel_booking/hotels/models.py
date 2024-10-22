from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from phonenumber_field.formfields import PhoneNumberField


ROLE_CHOICES = (
    ('клиент', 'Kлиент'),
    ('владелец', 'Владелец отеля'),
    ('админ', 'Aдмин'),
)


class UserProfile(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField()
    age = models.PositiveSmallIntegerField(default=0, null=True, blank=True,
                                           validators=[MinValueValidator(18),
                                                       MaxValueValidator(100)])
    date_registered = models.DateField(auto_now=True, null=True, blank=True)
    phone_number = PhoneNumberField()
    role = models.CharField(max_length=18, choices=ROLE_CHOICES, default='клиент')

    def __str__(self):
        return f'{self.first_name}-{self.last_name}'


class Hotel(models.Model):
    name_hotel = models.CharField(max_length=32)
    description = models.TextField()
    address = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    country = models.CharField(max_length=32)
    date = models.DateField(auto_now=True)
    price = models.PositiveIntegerField(default=0)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    active = models.BooleanField(default=True, verbose_name='в наличии')
    hotel_video = models.FileField(upload_to='hotel_videos/', verbose_name="Видео", null=True, blank=True)

    def __str__(self):
        return f'{self.name_hotel} - {self.country}'

    def get_average_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            return round(sum(review.stars for review in reviews) / reviews.count(), 1)
        return 0


class HotelPhotos(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='hotel', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='hotel_images')


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.SmallIntegerField(default=0)
    capacity = models.PositiveIntegerField(default=0)
    price_per_night = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.room_number}'


class RoomPhotos(models.Model):
    room = models.ForeignKey(Room, related_name='room', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='hotel_images')


class Review(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    parent_review = models.ForeignKey('self', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    stars = models.IntegerField(choices=[(i, str(1)) for i in range(1, 6)], verbose_name="Рейтинг")
    hotel = models.ForeignKey(Hotel, related_name='reviews', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author}'

