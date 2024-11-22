import uuid

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone

from app.managers import UserManager

# Create your models here.


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class User(AbstractUser, TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = None
    email = models.EmailField(unique=True)
    email_verified = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=100, blank=True, null=True)
    token_created_at = models.DateTimeField(blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    address = models.TextField()
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def generate_verification_code(self):
        self.verification_code = str(uuid.uuid4())
        self.token_created_at = timezone.now()
        self.save()

    def is_token_valid(self):
        if self.token_created_at:
            return (
                timezone.now() - self.token_created_at
            ) < timezone.timedelta(hours=24)
        return False


class Hotel(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    description = models.TextField()
    phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$')],
        help_text="Enter phone number in the format: '+999999999'. Up to 15 digits allowed."
    )
    

class Room(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    price_per_day = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)
    max_allowed = models.IntegerField()


class Booking(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    num_guests = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='confirmed')


class Review(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
